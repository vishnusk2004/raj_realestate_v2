from django.core.management.base import BaseCommand
from django.urls import reverse
from django.conf import settings
import urllib.parse


class Command(BaseCommand):
    help = 'Generate social media tracking URLs for testing the social media link tracking system'

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
            self.style.SUCCESS(f'🔗 Generating Social Media Tracking URLs for customer: {customer_code}')
        )
        self.stdout.write('=' * 70)
        
        # Define social media URLs
        social_media_urls = [
            {
                'platform': 'facebook',
                'url': 'https://facebook.com/rajrealestate',
                'description': 'Track Facebook page visits'
            },
            {
                'platform': 'instagram',
                'url': 'https://instagram.com/rajrealestate',
                'description': 'Track Instagram profile visits'
            },
            {
                'platform': 'twitter',
                'url': 'https://twitter.com/rajrealestate',
                'description': 'Track Twitter profile visits'
            },
            {
                'platform': 'linkedin',
                'url': 'https://linkedin.com/company/rajrealestate',
                'description': 'Track LinkedIn company page visits'
            },
            {
                'platform': 'telegram',
                'url': 'https://t.me/rajrealestate',
                'description': 'Track Telegram channel visits'
            },
            {
                'platform': 'youtube',
                'url': 'https://youtube.com/@rajrealestate',
                'description': 'Track YouTube channel visits'
            },
            {
                'platform': 'youtube',
                'url': 'https://www.youtube.com/watch?v=oSboc9BzlXc',
                'description': 'Track specific YouTube video visits'
            },
        ]
        
        self.stdout.write('\n📱 Sample Social Media Messages:')
        self.stdout.write('-' * 50)
        for social in social_media_urls[:2]:  # Show first 2 examples
            encoded_url = urllib.parse.quote(social['url'], safe='')
            tracking_url = f"{base_url}/{social['platform']}/{encoded_url}/{customer_code}"
            self.stdout.write(f'Follow us on {social["platform"].title()}: {tracking_url}')
        self.stdout.write('-' * 50)
        
        # Show example with unencoded URL (like the production issue)
        self.stdout.write('\n🔧 Production Example (Unencoded URL):')
        self.stdout.write('-' * 50)
        example_url = f"https://henry-realestate.onrender.com/facebook/https://www.facebook.com/share/1JAgT6ZhjL/{customer_code}"
        self.stdout.write(f"Facebook Share: {example_url}")
        self.stdout.write("✅ This format now works with mixed case customer codes!")
        
        self.stdout.write('\n🔗 Generated Social Media Tracking URLs:')
        self.stdout.write('-' * 70)
        
        for i, social in enumerate(social_media_urls, 1):
            # Encode the URL for the tracking URL
            encoded_url = urllib.parse.quote(social['url'], safe='')
            tracking_url = f"{base_url}/{social['platform']}/{encoded_url}/{customer_code}"
            
            self.stdout.write(f'{i}. {social["platform"].title()}')
            self.stdout.write(f'   Original URL: {social["url"]}')
            self.stdout.write(f'   Tracking URL: {tracking_url}')
            self.stdout.write(f'   Purpose: {social["description"]}')
            self.stdout.write('')
        
        self.stdout.write('\n📊 What happens when customer clicks:')
        self.stdout.write('-' * 60)
        self.stdout.write('1. Customer receives SMS with social media tracking URL')
        self.stdout.write('2. Customer clicks the tracking URL')
        self.stdout.write('3. System extracts customer code and platform')
        self.stdout.write('4. System records click with timestamp and system info')
        self.stdout.write('5. System sends tracking data to Podio CRM webhook')
        self.stdout.write('6. Customer is redirected to the actual social media URL')
        self.stdout.write('7. Customer sees the social media page')
        
        self.stdout.write('\n📈 Data sent to Podio CRM:')
        self.stdout.write('-' * 40)
        self.stdout.write('• Customer Code: NAE1495')
        self.stdout.write('• Platform: facebook, instagram, twitter, etc.')
        self.stdout.write('• Original URL: https://facebook.com/rajrealestate')
        self.stdout.write('• Click Count: 1')
        self.stdout.write('• IP Address: Customer IP')
        self.stdout.write('• User Agent: Browser info')
        self.stdout.write('• Timestamp: When clicked')
        
        self.stdout.write('\n✅ Social Media Tracking Ready!')
        self.stdout.write(f'📈 View tracking data at: {base_url}/admin/Henry/linktracking/')
        self.stdout.write('🔗 Link Tracking Webhook URL: https://workflow-automation.podio.com/catch/sajz0io9683p7b0')
