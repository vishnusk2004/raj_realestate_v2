from django.core.management.base import BaseCommand
from Raj.models import OpenHouse, OpenHouseImage


class Command(BaseCommand):
    help = 'Debug open house images to see what images are available'

    def add_arguments(self, parser):
        parser.add_argument('--open-house-id', type=int, help='Specific open house ID to debug')

    def handle(self, *args, **options):
        if options['open_house_id']:
            open_houses = OpenHouse.objects.filter(id=options['open_house_id'])
        else:
            open_houses = OpenHouse.objects.all()

        for open_house in open_houses:
            self.stdout.write(f"\n=== Open House: {open_house.title} (ID: {open_house.id}) ===")
            
            # Main image
            main_image_url = open_house.get_main_image_url()
            self.stdout.write(f"Main Image URL: {main_image_url}")
            
            # Additional images
            images = open_house.images.all()
            self.stdout.write(f"Number of additional images: {images.count()}")
            
            for i, image in enumerate(images, 1):
                self.stdout.write(f"\n  Image {i}:")
                self.stdout.write(f"    Caption: {image.caption}")
                self.stdout.write(f"    Is Primary: {image.is_primary}")
                self.stdout.write(f"    Order: {image.order}")
                self.stdout.write(f"    Image URL: {image.get_image_url()}")
                self.stdout.write(f"    Has Base64: {bool(image.image_base64)}")
                self.stdout.write(f"    Has File: {bool(image.image_file)}")
                self.stdout.write(f"    Has URL: {bool(image.image_url)}")
