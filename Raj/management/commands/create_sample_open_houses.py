from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time, timedelta
from Raj.models import OpenHouse


class Command(BaseCommand):
    help = 'Create sample open house events'

    def handle(self, *args, **options):
        # Create sample open house events
        open_houses_data = [
            {
                'title': 'Luxury Downtown Condo',
                'property_address': '123 Main Street, New York, NY 10001',
                'price': 850000.00,
                'bedrooms': 2,
                'bathrooms': 2,
                'area_sqft': 1200,
                'description': 'Beautiful luxury condo in the heart of downtown with stunning city views.',
                'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                'open_house_date': date.today() + timedelta(days=2),
                'open_house_time': time(10, 0),  # 10:00 AM
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'published': True
            },
            {
                'title': 'Family Home with Garden',
                'property_address': '456 Oak Avenue, Brooklyn, NY 11201',
                'price': 650000.00,
                'bedrooms': 3,
                'bathrooms': 2,
                'area_sqft': 1800,
                'description': 'Perfect family home with a beautiful garden and modern amenities.',
                'image_url': 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                'open_house_date': date.today() + timedelta(days=3),
                'open_house_time': time(14, 0),  # 2:00 PM
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'published': True
            },
            {
                'title': 'Modern Townhouse',
                'property_address': '789 Pine Street, Queens, NY 11375',
                'price': 750000.00,
                'bedrooms': 4,
                'bathrooms': 3,
                'area_sqft': 2200,
                'description': 'Contemporary townhouse with open floor plan and premium finishes.',
                'image_url': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                'open_house_date': date.today() + timedelta(days=4),
                'open_house_time': time(11, 0),  # 11:00 AM
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'published': True
            }
        ]

        created_count = 0
        for house_data in open_houses_data:
            open_house, created = OpenHouse.objects.get_or_create(
                title=house_data['title'],
                defaults=house_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created open house: {open_house.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Open house already exists: {open_house.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} open house events')
        )
