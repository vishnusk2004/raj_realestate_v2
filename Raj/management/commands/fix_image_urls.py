#!/usr/bin/env python
"""
Management command to fix image URLs for OpenHouse properties
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from Raj.models import OpenHouse, OpenHouseImage
import os

class Command(BaseCommand):
    help = 'Fix image URLs for OpenHouse properties'

    def handle(self, *args, **options):
        self.stdout.write("🔧 Fixing image URLs for OpenHouse properties...")
        
        # Check OpenHouse main images
        open_houses = OpenHouse.objects.all()
        fixed_count = 0
        
        for oh in open_houses:
            self.stdout.write(f"\n📋 Checking: {oh.title}")
            
            # Check main image
            if oh.image_file and oh.image_file.name:
                file_path = os.path.join(settings.MEDIA_ROOT, oh.image_file.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"  ✅ Main image file exists: {oh.image_file.name}")
                else:
                    self.stdout.write(f"  ❌ Main image file missing: {oh.image_file.name}")
                    if oh.image_url:
                        self.stdout.write(f"  🔄 Falling back to URL: {oh.image_url}")
                        # Clear the file reference to force URL usage
                        oh.image_file = None
                        oh.save()
                        fixed_count += 1
            
            # Check gallery images
            for img in oh.images.all():
                if img.image_file and img.image_file.name:
                    file_path = os.path.join(settings.MEDIA_ROOT, img.image_file.name)
                    if os.path.exists(file_path):
                        self.stdout.write(f"  ✅ Gallery image file exists: {img.image_file.name}")
                    else:
                        self.stdout.write(f"  ❌ Gallery image file missing: {img.image_file.name}")
                        if img.image_url:
                            self.stdout.write(f"  🔄 Falling back to URL: {img.image_url}")
                            # Clear the file reference to force URL usage
                            img.image_file = None
                            img.save()
                            fixed_count += 1
        
        self.stdout.write(f"\n✅ Fixed {fixed_count} image references")
        self.stdout.write("🎉 Image URL fixing completed!")
