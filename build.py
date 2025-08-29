#!/usr/bin/env python
"""
Build script for Vercel deployment
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Collect static files
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])

print("Build completed successfully!")
