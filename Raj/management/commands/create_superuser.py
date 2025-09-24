#!/usr/bin/env python
"""
Management command to create a superuser for production deployment
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create a superuser for production deployment'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default=os.getenv('ADMIN_USERNAME', 'admin'),
            help='Username for the superuser (default: admin or ADMIN_USERNAME env var)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default=os.getenv('ADMIN_EMAIL', 'admin@example.com'),
            help='Email for the superuser (default: admin@example.com or ADMIN_EMAIL env var)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default=os.getenv('ADMIN_PASSWORD', 'admin123'),
            help='Password for the superuser (default: admin123 or ADMIN_PASSWORD env var)'
        )
        parser.add_argument(
            '--noinput',
            action='store_true',
            help='Run without user input (use environment variables)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        noinput = options['noinput']

        # Check if superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists. Skipping creation.')
            )
            return

        # Create superuser
        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser "{username}"')
            )
            
            if not noinput:
                self.stdout.write(
                    self.style.WARNING(
                        f'Admin credentials:\n'
                        f'Username: {username}\n'
                        f'Email: {email}\n'
                        f'Password: {password}\n'
                        f'Admin URL: /admin/'
                    )
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
            raise
