#!/usr/bin/env python
"""
Data migration script to transfer data from SQLite to PostgreSQL
"""
import os
import sys
import django
import json

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# Force SQLite for local export
os.environ['VERCEL'] = 'false'
django.setup()

from Raj.models import Property, SellingContact
from django.core.management import execute_from_command_line

def export_data():
    """Export data from SQLite to JSON"""
    print("Exporting data from SQLite...")
    
    # Export properties
    properties = Property.objects.all()
    properties_data = []
    
    for prop in properties:
        properties_data.append({
            'address': prop.address,
            'price': str(prop.price),
            'bedrooms': prop.bedrooms,
            'bathrooms': prop.bathrooms,
            'square_feet': prop.square_feet,
            'property_type': prop.property_type,
            'status': prop.status,
            'description': prop.description,
            'image_url': prop.image_url,
            'created_at': prop.created_at.isoformat() if prop.created_at else None,
            'updated_at': prop.updated_at.isoformat() if prop.updated_at else None,
        })
    
    # Save to JSON file
    with open('properties_data.json', 'w') as f:
        json.dump(properties_data, f, indent=2)
    
    print(f"Exported {len(properties_data)} properties to properties_data.json")

if __name__ == "__main__":
    export_data()
