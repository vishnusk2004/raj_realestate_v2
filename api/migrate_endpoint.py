#!/usr/bin/env python
"""
API endpoint to run migrations
"""
import os
import sys
import django
from django.http import JsonResponse

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.core.management import execute_from_command_line

def run_migrations(request):
    """Run Django migrations"""
    try:
        print("Running Django migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        return JsonResponse({"status": "success", "message": "Migrations completed successfully!"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
