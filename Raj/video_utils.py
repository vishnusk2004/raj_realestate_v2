#!/usr/bin/env python
"""
Utility functions for handling video compression and optimization
"""
import os
import subprocess
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import sys

def compress_video(video_file, max_size_mb=50, quality='medium'):
    """
    Compress video file to reduce size
    
    Args:
        video_file: Django FileField or file path
        max_size_mb: Maximum file size in MB (default: 50MB)
        quality: Compression quality - 'low', 'medium', 'high' (default: 'medium')
        
    Returns:
        ContentFile: Compressed video file or None if compression fails
    """
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      capture_output=True, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: ffmpeg not found. Video compression skipped.")
        print("To enable video compression, install ffmpeg:")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt-get install ffmpeg")
        return None
    
    try:
        # Get file path
        if hasattr(video_file, 'path'):
            input_path = video_file.path
        elif hasattr(video_file, 'name'):
            input_path = video_file.name
        else:
            input_path = str(video_file)
        
        # Create output path
        output_path = input_path.replace('.', '_compressed.')
        
        # Quality settings
        quality_settings = {
            'low': ['-crf', '28', '-preset', 'fast'],
            'medium': ['-crf', '23', '-preset', 'medium'],
            'high': ['-crf', '18', '-preset', 'slow']
        }
        
        # Build ffmpeg command
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libx264',  # H.264 codec
            '-c:a', 'aac',      # AAC audio codec
            '-movflags', '+faststart',  # Optimize for web streaming
            '-max_muxing_queue_size', '1024',
        ] + quality_settings.get(quality, quality_settings['medium'])
        
        # Add output path
        cmd.append(output_path)
        
        # Run ffmpeg
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check output file size
        if os.path.exists(output_path):
            file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
            
            # If still too large, compress more aggressively
            if file_size_mb > max_size_mb:
                return compress_video(output_path, max_size_mb, 'low')
            
            # Read compressed file
            with open(output_path, 'rb') as f:
                compressed_data = f.read()
            
            # Clean up temporary file
            if output_path != input_path:
                try:
                    os.remove(output_path)
                except:
                    pass
            
            # Create ContentFile
            filename = os.path.basename(input_path)
            return ContentFile(compressed_data, name=filename)
        
        return None
        
    except Exception as e:
        print(f"Error compressing video: {e}")
        return None

def get_video_info(video_file):
    """
    Get video information (duration, resolution, size, etc.)
    
    Args:
        video_file: Django FileField or file path
        
    Returns:
        dict: Video information or None if ffprobe not available
    """
    # Check if ffprobe is available
    try:
        subprocess.run(['ffprobe', '-version'], 
                      capture_output=True, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    
    try:
        # Get file path
        if hasattr(video_file, 'path'):
            input_path = video_file.path
        elif hasattr(video_file, 'name'):
            input_path = video_file.name
        else:
            input_path = str(video_file)
        
        # Run ffprobe
        cmd = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            input_path
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        import json
        info = json.loads(result.stdout)
        
        # Extract useful information
        video_info = {
            'duration': float(info.get('format', {}).get('duration', 0)),
            'size': int(info.get('format', {}).get('size', 0)),
            'bitrate': int(info.get('format', {}).get('bit_rate', 0)),
        }
        
        # Get video stream info
        for stream in info.get('streams', []):
            if stream.get('codec_type') == 'video':
                video_info['width'] = int(stream.get('width', 0))
                video_info['height'] = int(stream.get('height', 0))
                video_info['codec'] = stream.get('codec_name', '')
                break
        
        return video_info
        
    except Exception as e:
        print(f"Error getting video info: {e}")
        return None

