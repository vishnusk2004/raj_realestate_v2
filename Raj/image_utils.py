#!/usr/bin/env python
"""
Utility functions for handling image conversion to/from base64
"""
import base64
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import os

def image_to_base64(image_field):
    """
    Convert a Django ImageField to base64 string
    
    Args:
        image_field: Django ImageField instance
        
    Returns:
        str: Base64 encoded image data with data URL prefix
    """
    if not image_field or not image_field.name:
        return None
    
    try:
        # Open the image file
        image = Image.open(image_field)
        
        # Convert to RGB if necessary (for PNG with transparency)
        if image.mode in ('RGBA', 'LA', 'P'):
            image = image.convert('RGB')
        
        # Resize image to reasonable size (max 1200px width, maintain aspect ratio)
        # For web display, we can be more aggressive with compression
        max_width = 1200
        max_height = 1200
        if image.width > max_width or image.height > max_height:
            # Calculate ratio to fit within max dimensions
            width_ratio = max_width / image.width if image.width > max_width else 1
            height_ratio = max_height / image.height if image.height > max_height else 1
            ratio = min(width_ratio, height_ratio)
            new_width = int(image.width * ratio)
            new_height = int(image.height * ratio)
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Convert to base64 with optimized compression
        # Quality 80 provides good balance between file size and visual quality
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG', quality=80, optimize=True, progressive=True)
        buffer.seek(0)
        
        # Encode to base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # Return as data URL
        return f"data:image/jpeg;base64,{image_base64}"
        
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

def base64_to_image(base64_string):
    """
    Convert base64 string back to PIL Image object
    
    Args:
        base64_string: Base64 encoded image data with or without data URL prefix
        
    Returns:
        PIL.Image: Image object or None if conversion fails
    """
    if not base64_string:
        return None
    
    try:
        # Remove data URL prefix if present
        if base64_string.startswith('data:image/'):
            base64_string = base64_string.split(',')[1]
        
        # Decode base64
        image_data = base64.b64decode(base64_string)
        
        # Create PIL Image
        image = Image.open(io.BytesIO(image_data))
        
        return image
        
    except Exception as e:
        print(f"Error converting base64 to image: {e}")
        return None

def save_base64_to_image_field(base64_string, field_name):
    """
    Convert base64 string to Django ImageField content
    
    Args:
        base64_string: Base64 encoded image data
        field_name: Name for the file
        
    Returns:
        ContentFile: Django ContentFile object ready for ImageField
    """
    if not base64_string:
        return None
    
    try:
        # Remove data URL prefix if present
        if base64_string.startswith('data:image/'):
            base64_string = base64_string.split(',')[1]
        
        # Decode base64
        image_data = base64.b64decode(base64_string)
        
        # Create ContentFile
        return ContentFile(image_data, name=f"{field_name}.jpg")
        
    except Exception as e:
        print(f"Error creating ContentFile from base64: {e}")
        return None

def get_image_data_url(base64_string):
    """
    Ensure base64 string has proper data URL prefix
    
    Args:
        base64_string: Base64 encoded image data
        
    Returns:
        str: Properly formatted data URL
    """
    if not base64_string:
        return None
    
    if base64_string.startswith('data:image/'):
        return base64_string
    
    return f"data:image/jpeg;base64,{base64_string}"
