#!/usr/bin/env python
"""
Migration script for Vercel deployment
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Run migrations
from django.core.management import execute_from_command_line

print("Running Django migrations...")
execute_from_command_line(['manage.py', 'migrate'])

print("Migrations completed successfully!")
