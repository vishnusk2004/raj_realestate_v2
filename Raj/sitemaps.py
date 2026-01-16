from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost

class MainViewSitemap(Sitemap):
    priority = 1.0       # Highest priority for Home
    changefreq = 'daily'
    protocol = 'https'   # Force HTTPS for SEO

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class StaticViewSitemap(Sitemap):
    priority = 0.8       # High priority for main landing pages
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return [
            'buying',
            'selling',
            'leasing',
            'open_house',
            'market_insights',
            'mortgage_calculator',
            'blog',
        ]

    def location(self, item):
        return reverse(item)

class LegalSitemap(Sitemap):
    priority = 0.3       # Low priority for legal pages
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return [
            'terms_of_service',
            'privacy_policy',
            'cookie_policy',
        ]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 0.6       # Medium priority for blog posts
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return BlogPost.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('blog_detail', args=[obj.id])