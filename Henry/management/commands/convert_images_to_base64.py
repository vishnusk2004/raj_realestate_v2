#!/usr/bin/env python
"""
Management command to convert existing uploaded images to base64
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from Henry.models import OpenHouse, OpenHouseImage, PropertyListing, PropertyListingImage
from Henry.image_utils import image_to_base64
import os

class Command(BaseCommand):
    help = 'Convert existing uploaded images to base64 format'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be converted without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write("🔍 DRY RUN MODE - No changes will be made")
        
        self.stdout.write("🖼️ Converting images to base64...")
        
        # Convert PropertyListing images
        property_listings = PropertyListing.objects.filter(image_file__isnull=False).exclude(image_file='')
        converted_count = 0
        
        for pl in property_listings:
            if pl.image_file and pl.image_file.name and not pl.image_base64:
                self.stdout.write(f"\n📋 Converting property image for: {pl.title}")
                
                # Check if file exists
                file_path = os.path.join(settings.MEDIA_ROOT, pl.image_file.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"  ✅ File exists: {pl.image_file.name}")
                    
                    if not dry_run:
                        # Convert to base64
                        base64_data = image_to_base64(pl.image_file)
                        if base64_data:
                            pl.image_base64 = base64_data
                            pl.save()
                            self.stdout.write(f"  ✅ Converted to base64")
                            converted_count += 1
                        else:
                            self.stdout.write(f"  ❌ Failed to convert to base64")
                    else:
                        self.stdout.write(f"  🔄 Would convert to base64")
                        converted_count += 1
                else:
                    self.stdout.write(f"  ❌ File missing: {pl.image_file.name}")
        
        # Convert OpenHouse main images
        open_houses = OpenHouse.objects.filter(image_file__isnull=False).exclude(image_file='')
        
        for oh in open_houses:
            if oh.image_file and oh.image_file.name and not oh.image_base64:
                self.stdout.write(f"\n📋 Converting main image for: {oh.title}")
                
                # Check if file exists
                file_path = os.path.join(settings.MEDIA_ROOT, oh.image_file.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"  ✅ File exists: {oh.image_file.name}")
                    
                    if not dry_run:
                        # Convert to base64
                        base64_data = image_to_base64(oh.image_file)
                        if base64_data:
                            oh.image_base64 = base64_data
                            oh.save()
                            self.stdout.write(f"  ✅ Converted to base64")
                            converted_count += 1
                        else:
                            self.stdout.write(f"  ❌ Failed to convert to base64")
                    else:
                        self.stdout.write(f"  🔄 Would convert to base64")
                        converted_count += 1
                else:
                    self.stdout.write(f"  ❌ File missing: {oh.image_file.name}")
        
        # Convert OpenHouseImage gallery images
        gallery_images = OpenHouseImage.objects.filter(image_file__isnull=False).exclude(image_file='')
        
        for img in gallery_images:
            if img.image_file and img.image_file.name and not img.image_base64:
                self.stdout.write(f"\n📋 Converting gallery image for: {img.open_house.title}")
                
                # Check if file exists
                file_path = os.path.join(settings.MEDIA_ROOT, img.image_file.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"  ✅ File exists: {img.image_file.name}")
                    
                    if not dry_run:
                        # Convert to base64
                        base64_data = image_to_base64(img.image_file)
                        if base64_data:
                            img.image_base64 = base64_data
                            img.save()
                            self.stdout.write(f"  ✅ Converted to base64")
                            converted_count += 1
                        else:
                            self.stdout.write(f"  ❌ Failed to convert to base64")
                    else:
                        self.stdout.write(f"  🔄 Would convert to base64")
                        converted_count += 1
                else:
                    self.stdout.write(f"  ❌ File missing: {img.image_file.name}")
        
        # Convert PropertyListingImage gallery images
        property_listing_images = PropertyListingImage.objects.filter(image_file__isnull=False).exclude(image_file='')
        
        for pli in property_listing_images:
            if pli.image_file and pli.image_file.name and not pli.image_base64:
                self.stdout.write(f"\n📋 Converting gallery image for: {pli.property_listing.title}")
                
                # Check if file exists
                file_path = os.path.join(settings.MEDIA_ROOT, pli.image_file.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"  ✅ File exists: {pli.image_file.name}")
                    
                    if not dry_run:
                        # Convert to base64
                        base64_data = image_to_base64(pli.image_file)
                        if base64_data:
                            pli.image_base64 = base64_data
                            pli.save()
                            self.stdout.write(f"  ✅ Converted to base64")
                            converted_count += 1
                        else:
                            self.stdout.write(f"  ❌ Failed to convert to base64")
                    else:
                        self.stdout.write(f"  🔄 Would convert to base64")
                        converted_count += 1
                else:
                    self.stdout.write(f"  ❌ File missing: {pli.image_file.name}")
        
        if dry_run:
            self.stdout.write(f"\n🔍 DRY RUN: Would convert {converted_count} images to base64")
        else:
            self.stdout.write(f"\n✅ Successfully converted {converted_count} images to base64")
        
        self.stdout.write("🎉 Image conversion completed!")
