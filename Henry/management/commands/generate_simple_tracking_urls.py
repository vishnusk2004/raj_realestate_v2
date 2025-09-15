#!/usr/bin/env python
"""
Management command to generate simple tracking URLs
Format: https://domain.com/?url=https://target.com&code=customer_code
"""
from django.core.management.base import BaseCommand
import urllib.parse


class Command(BaseCommand):
    help = 'Generate simple tracking URLs for easy sharing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--customer-code',
            type=str,
            required=True,
            help='Customer code (e.g., ju123, NAE1495)'
        )
        parser.add_argument(
            '--base-url',
            type=str,
            default='https://henry-realestate.onrender.com',
            help='Base URL for tracking (default: https://henry-realestate.onrender.com)'
        )

    def handle(self, *args, **options):
        customer_code = options['customer_code']
        base_url = options['base_url']
        
        self.stdout.write(
            self.style.SUCCESS(f'🔗 Generating Simple Tracking URLs for customer: {customer_code}')
        )
        self.stdout.write('=' * 70)
        
        # Define tracking URLs (both internal and external)
        tracking_urls = [
            # Internal Pages
            {
                'platform': 'Home Page',
                'url': f'{base_url}/',
                'description': 'Track home page visits'
            },
            {
                'platform': 'Blog Post',
                'url': f'{base_url}/blog/2/',
                'description': 'Track specific blog post visits'
            },
            {
                'platform': 'Selling Page',
                'url': f'{base_url}/selling/',
                'description': 'Track selling page visits'
            },
            {
                'platform': 'Buy/Lease Page',
                'url': f'{base_url}/buy-lease/',
                'description': 'Track buy/lease page visits'
            },
            {
                'platform': 'Open House',
                'url': f'{base_url}/open-house/',
                'description': 'Track open house page visits'
            },
            {
                'platform': 'Mortgage Calculator',
                'url': f'{base_url}/mortgage-calculator/',
                'description': 'Track mortgage calculator visits'
            },
            # Social Media
            {
                'platform': 'Facebook',
                'url': 'https://facebook.com/rajrealestate',
                'description': 'Track Facebook page visits'
            },
            {
                'platform': 'Instagram',
                'url': 'https://instagram.com/rajrealestate',
                'description': 'Track Instagram profile visits'
            },
            {
                'platform': 'Twitter',
                'url': 'https://twitter.com/rajrealestate',
                'description': 'Track Twitter profile visits'
            },
            {
                'platform': 'LinkedIn',
                'url': 'https://linkedin.com/company/rajrealestate',
                'description': 'Track LinkedIn company page visits'
            },
            {
                'platform': 'Telegram',
                'url': 'https://t.me/rajrealestate',
                'description': 'Track Telegram channel visits'
            },
            {
                'platform': 'YouTube',
                'url': 'https://youtube.com/@rajrealestate',
                'description': 'Track YouTube channel visits'
            },
            {
                'platform': 'YouTube Video',
                'url': 'https://www.youtube.com/watch?v=oSboc9BzlXc',
                'description': 'Track specific YouTube video visits'
            },
            {
                'platform': 'Facebook Share',
                'url': 'https://www.facebook.com/share/1JAgT6ZhjL',
                'description': 'Track Facebook share link'
            },
        ]
        
        self.stdout.write('\n📱 Sample Simple Tracking URLs:')
        self.stdout.write('-' * 50)
        
        for item in tracking_urls[:3]:  # Show first 3 examples
            encoded_url = urllib.parse.quote(item['url'], safe='')
            tracking_url = f"{base_url}/?url={encoded_url}&code={customer_code}"
            self.stdout.write(f'{item["platform"]}: {tracking_url}')
        
        self.stdout.write('-' * 50)
        
        self.stdout.write('\n🔗 All Simple Tracking URLs:')
        self.stdout.write('-' * 70)
        
        for i, item in enumerate(tracking_urls, 1):
            # Encode the URL for the tracking URL
            encoded_url = urllib.parse.quote(item['url'], safe='')
            tracking_url = f"{base_url}/?url={encoded_url}&code={customer_code}"
            
            self.stdout.write(f'{i}. {item["platform"]}')
            self.stdout.write(f'   Original URL: {item["url"]}')
            self.stdout.write(f'   Tracking URL: {tracking_url}')
            self.stdout.write(f'   Purpose: {item["description"]}')
            self.stdout.write('')
        
        self.stdout.write('\n📊 How Simple Tracking Works:')
        self.stdout.write('-' * 50)
        self.stdout.write('1. Customer receives simple tracking URL')
        self.stdout.write('2. Customer clicks the tracking URL')
        self.stdout.write('3. System extracts URL and customer code from query parameters')
        self.stdout.write('4. System determines platform from target URL')
        self.stdout.write('5. System records click with timestamp and system info')
        self.stdout.write('6. System sends tracking data to Podio CRM webhook')
        self.stdout.write('7. Customer is redirected to the actual target URL')
        self.stdout.write('8. Customer sees the target page')
        
        self.stdout.write('\n📈 Data sent to Podio CRM:')
        self.stdout.write('-' * 50)
        self.stdout.write(f'• Customer Code: {customer_code}')
        self.stdout.write('• Platform: facebook, instagram, twitter, etc.')
        self.stdout.write('• Original URL: https://facebook.com/rajrealestate')
        self.stdout.write('• Click Count: 1')
        self.stdout.write('• IP Address: Customer IP')
        self.stdout.write('• User Agent: Browser info')
        self.stdout.write('• Timestamp: When clicked')
        
        self.stdout.write('\n✅ Simple Tracking Ready!')
        self.stdout.write(f'📈 View tracking data at: {base_url}/admin/Henry/linktracking/')
        self.stdout.write('🔗 Podio webhook URL: https://workflow-automation.podio.com/catch/8g78a8102321zec')
        
        self.stdout.write('\n💡 Benefits of Simple URLs:')
        self.stdout.write('-' * 50)
        self.stdout.write('✅ Shorter and cleaner URLs')
        self.stdout.write('✅ Easy to read and understand')
        self.stdout.write('✅ No URL encoding issues')
        self.stdout.write('✅ Works with any target URL')
        self.stdout.write('✅ Same tracking functionality')
