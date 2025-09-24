from django.core.management.base import BaseCommand
from Raj.models import PropertyListing, PropertyListingImage
from Raj.image_utils import image_to_base64
import os

class Command(BaseCommand):
    help = 'Convert all existing image files to base64 format'

    def handle(self, *args, **options):
        self.stdout.write('Starting image conversion to base64...')
        
        # Convert PropertyListing images
        properties = PropertyListing.objects.all()
        converted_count = 0
        
        for property_obj in properties:
            # Convert main image
            if property_obj.image_file and property_obj.image_file.name and not property_obj.image_base64:
                try:
                    base64_data = image_to_base64(property_obj.image_file)
                    if base64_data:
                        property_obj.image_base64 = base64_data
                        property_obj.save(update_fields=['image_base64'])
                        converted_count += 1
                        self.stdout.write(f'Converted main image for: {property_obj.title}')
                except Exception as e:
                    self.stdout.write(f'Error converting main image for {property_obj.title}: {e}')
            
            # Convert related images
            for img in property_obj.images.all():
                if img.image_file and img.image_file.name and not img.image_base64:
                    try:
                        base64_data = image_to_base64(img.image_file)
                        if base64_data:
                            img.image_base64 = base64_data
                            img.save(update_fields=['image_base64'])
                            converted_count += 1
                            self.stdout.write(f'Converted related image for: {property_obj.title}')
                    except Exception as e:
                        self.stdout.write(f'Error converting related image for {property_obj.title}: {e}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully converted {converted_count} images to base64 format')
        )