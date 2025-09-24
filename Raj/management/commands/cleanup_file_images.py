from django.core.management.base import BaseCommand
from Raj.models import PropertyListing, PropertyListingImage
import os

class Command(BaseCommand):
    help = 'Clean up file-based images after converting to base64'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write('DRY RUN - No files will be deleted')
        
        # Clean up PropertyListing images
        properties = PropertyListing.objects.all()
        cleaned_count = 0
        
        for property_obj in properties:
            if property_obj.image_file and property_obj.image_file.name and property_obj.image_base64:
                file_path = property_obj.image_file.path
                if os.path.exists(file_path):
                    if dry_run:
                        self.stdout.write(f'Would delete: {file_path}')
                    else:
                        try:
                            os.remove(file_path)
                            self.stdout.write(f'Deleted: {file_path}')
                            cleaned_count += 1
                        except Exception as e:
                            self.stdout.write(f'Error deleting {file_path}: {e}')
            
            # Clean up related images
            for img in property_obj.images.all():
                if img.image_file and img.image_file.name and img.image_base64:
                    file_path = img.image_file.path
                    if os.path.exists(file_path):
                        if dry_run:
                            self.stdout.write(f'Would delete: {file_path}')
                        else:
                            try:
                                os.remove(file_path)
                                self.stdout.write(f'Deleted: {file_path}')
                                cleaned_count += 1
                            except Exception as e:
                                self.stdout.write(f'Error deleting {file_path}: {e}')
        
        if dry_run:
            self.stdout.write(f'Would clean up {cleaned_count} image files')
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully cleaned up {cleaned_count} image files')
            )
