from django.core.management.base import BaseCommand
from Henry.models import PropertyListing


class Command(BaseCommand):
    help = 'Create sample property listings for Buy/Lease section'

    def handle(self, *args, **options):
        # Sample properties for sale
        properties_for_sale = [
            {
                'title': 'Modern Downtown Condo',
                'property_type': 'buy',
                'price': 450000.00,
                'location': 'Downtown Toronto',
                'address': '123 King Street West, Toronto, ON M5H 1A1',
                'bedrooms': 2,
                'bathrooms': 2,
                'parking_spaces': 1,
                'area_sqft': 1200,
                'description': 'Beautiful modern condo in the heart of downtown Toronto. Features floor-to-ceiling windows, granite countertops, and a stunning city view. Walking distance to restaurants, shopping, and public transit.',
                'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&h=600&fit=crop',
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'featured': True,
                'published': True
            },
            {
                'title': 'Family Home in Suburbs',
                'property_type': 'buy',
                'price': 750000.00,
                'location': 'Mississauga',
                'address': '456 Oak Street, Mississauga, ON L5B 2C3',
                'bedrooms': 4,
                'bathrooms': 3,
                'parking_spaces': 2,
                'area_sqft': 2200,
                'description': 'Perfect family home with a large backyard, finished basement, and updated kitchen. Located in a quiet neighborhood with excellent schools nearby.',
                'image_url': 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800&h=600&fit=crop',
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'featured': False,
                'published': True
            },
            {
                'title': 'Luxury Penthouse Suite',
                'property_type': 'buy',
                'price': 1200000.00,
                'location': 'Yorkville',
                'address': '789 Bay Street, Toronto, ON M5G 1M5',
                'bedrooms': 3,
                'bathrooms': 3,
                'parking_spaces': 2,
                'area_sqft': 1800,
                'description': 'Stunning penthouse with panoramic city views, private terrace, and premium finishes throughout. Includes concierge service and access to building amenities.',
                'image_url': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&h=600&fit=crop',
                'contact_email': 'raj.gupta@kw.com',
                'contact_phone': '(832) 785-0140',
                'featured': True,
                'published': True
            }
        ]

        # Sample properties for lease
        properties_for_lease = [
            {
                'title': 'Furnished Studio Apartment',
                'property_type': 'lease',
                'price': 2200.00,
                'location': 'Entertainment District',
                'address': '321 Queen Street West, Toronto, ON M5V 2A5',
                'bedrooms': 0,
                'bathrooms': 1,
                'parking_spaces': 0,
                'area_sqft': 600,
                'description': 'Fully furnished studio apartment in the heart of the Entertainment District. Perfect for young professionals. Includes all utilities and high-speed internet.',
                'image_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&h=600&fit=crop',
                'contact_email': 'raj@the-bandpteam.com',
                'contact_phone': '(832) 785-0140',
                'featured': False,
                'published': True
            },
            {
                'title': 'Spacious 2-Bedroom Apartment',
                'property_type': 'lease',
                'price': 3200.00,
                'location': 'North York',
                'address': '654 Yonge Street, Toronto, ON M4Y 1Z9',
                'bedrooms': 2,
                'bathrooms': 2,
                'parking_spaces': 1,
                'area_sqft': 1100,
                'description': 'Bright and spacious 2-bedroom apartment with in-suite laundry, balcony, and parking. Close to subway station and shopping centers.',
                'image_url': 'https://images.unsplash.com/photo-1560448204-603b3fc33ddc?w=800&h=600&fit=crop',
                'contact_email': 'raj@the-bandpteam.com',
                'contact_phone': '(832) 785-0140',
                'featured': True,
                'published': True
            },
            {
                'title': 'Executive Townhouse',
                'property_type': 'lease',
                'price': 4500.00,
                'location': 'Richmond Hill',
                'address': '987 Major Mackenzie Drive, Richmond Hill, ON L4C 9X8',
                'bedrooms': 3,
                'bathrooms': 3,
                'parking_spaces': 2,
                'area_sqft': 1800,
                'description': 'Executive townhouse with modern finishes, private garage, and backyard. Ideal for families or professionals seeking luxury living.',
                'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&h=600&fit=crop',
                'contact_email': 'raj@the-bandpteam.com',
                'contact_phone': '(832) 785-0140',
                'featured': False,
                'published': True
            }
        ]

        # Create properties for sale
        for prop_data in properties_for_sale:
            property_obj, created = PropertyListing.objects.get_or_create(
                title=prop_data['title'],
                defaults=prop_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created property: {property_obj.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Property already exists: {property_obj.title}')
                )

        # Create properties for lease
        for prop_data in properties_for_lease:
            property_obj, created = PropertyListing.objects.get_or_create(
                title=prop_data['title'],
                defaults=prop_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created property: {property_obj.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Property already exists: {property_obj.title}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample property listings!')
        )

