from django.core.management.base import BaseCommand
from django.urls import reverse
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate sample tracking URLs for testing the link tracking system'

    def add_arguments(self, parser):
        parser.add_argument(
            '--customer-code',
            type=str,
            default='NAE1495',
            help='Customer code to use in the tracking URLs (default: NAE1495)'
        )
        parser.add_argument(
            '--base-url',
            type=str,
            default='http://127.0.0.1:8015',
            help='Base URL for the tracking links (default: http://127.0.0.1:8015)'
        )

    def handle(self, *args, **options):
        customer_code = options['customer_code']
        base_url = options['base_url']
        
        self.stdout.write(
            self.style.SUCCESS(f'🔗 Generating tracking URLs for customer: {customer_code}')
        )
        self.stdout.write('=' * 60)
        
        # Define the tracking URL patterns
        tracking_urls = [
            {
                'name': 'Blog Post #2',
                'url': f'{base_url}/blog/2/{customer_code}',
                'description': 'Track clicks on specific blog post'
            },
            {
                'name': 'Buy/Lease Page',
                'url': f'{base_url}/buy-lease/{customer_code}',
                'description': 'Track interest in buying/leasing properties'
            },
            {
                'name': 'Selling Page',
                'url': f'{base_url}/selling/{customer_code}',
                'description': 'Track interest in selling properties'
            },
            {
                'name': 'Open House Page',
                'url': f'{base_url}/open-house/{customer_code}',
                'description': 'Track interest in open house events'
            },
            {
                'name': 'Mortgage Calculator',
                'url': f'{base_url}/mortgage-calculator/{customer_code}',
                'description': 'Track mortgage calculation usage'
            },
            {
                'name': 'Home Page',
                'url': f'{base_url}/{customer_code}',
                'description': 'Track general website visits'
            },
        ]
        
        self.stdout.write('\n📱 Sample SMS Message:')
        self.stdout.write('-' * 40)
        self.stdout.write(f'Hello Naeem')
        self.stdout.write(f'I hope you are doing well...')
        self.stdout.write(f'Check out our latest blog post: {tracking_urls[0]["url"]}')
        self.stdout.write('-' * 40)
        
        self.stdout.write('\n🔗 Generated Tracking URLs:')
        self.stdout.write('-' * 60)
        
        for i, url_info in enumerate(tracking_urls, 1):
            self.stdout.write(f'{i}. {url_info["name"]}')
            self.stdout.write(f'   URL: {url_info["url"]}')
            self.stdout.write(f'   Purpose: {url_info["description"]}')
            self.stdout.write('')
        
        self.stdout.write('\n📊 What happens when customer clicks:')
        self.stdout.write('-' * 50)
        self.stdout.write('1. System extracts customer code from URL')
        self.stdout.write('2. Records click with timestamp and system info')
        self.stdout.write('3. Redirects customer to clean URL (no tracking code)')
        self.stdout.write('4. Customer sees normal page')
        self.stdout.write('5. Admin can view tracking data in dashboard')
        
        self.stdout.write('\n✅ Ready to send these URLs to customers!')
        self.stdout.write(f'📈 View tracking data at: {base_url}/admin/Henry/linktracking/')
