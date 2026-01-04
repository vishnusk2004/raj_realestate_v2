import re
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from .models import LinkTracking
from .webhook_utils import get_client_ip, send_link_tracking_to_crm


class LinkTrackingMiddleware(MiddlewareMixin):
    """
    Middleware to handle customer tracking codes in URLs
    Extracts codes like NAE1495 from URLs and tracks clicks
    """
    
    def process_request(self, request):
        # Skip admin URLs and other system URLs
        path = request.path
        if path.startswith('/admin/') or path.startswith('/static/') or path.startswith('/media/'):
            return None
            
        # Check for simple tracking format: /?url=https://facebook.com/page&code=ju123
        # Also supports internal pages: /?url=/blog/2/&code=ju123
        if path == '/' and request.GET.get('url') and request.GET.get('code'):
            url = request.GET.get('url')
            customer_code = request.GET.get('code')
            if not customer_code.startswith('u-'):
                return None
            
            # Determine if it's an internal or external URL
            if url.startswith('/') or url.startswith(request.get_host()):
                # Internal URL - determine page type and ID
                page_type, page_id = self._get_internal_page_info(url, request)
                original_url = url if url.startswith('http') else request.build_absolute_uri(url)
            else:
                # External URL - determine platform
                page_type = self._get_platform_from_url(url)
                page_id = None
                original_url = url
            
            if page_type:
                # Get system information
                ip_address = get_client_ip(request)
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                referrer = request.META.get('HTTP_REFERER', '')
                language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0] if request.META.get('HTTP_ACCEPT_LANGUAGE') else ''
                
                # Create or update tracking record
                tracking_record, created = LinkTracking.objects.get_or_create(
                    customer_code=customer_code,
                    page_type=page_type,
                    page_id=page_id,
                    defaults={
                        'original_url': original_url,
                        'tracked_url': request.build_absolute_uri(),
                    }
                )
                
                tracking_record.record_click(
                    ip_address=ip_address,
                    user_agent=user_agent,
                    referrer=referrer,
                    language=language
                )
                
                try:
                    send_link_tracking_to_crm(tracking_record, request)
                except Exception as e:
                    logger.error(f"Failed to send link tracking to CRM: {str(e)}")
                
                return HttpResponseRedirect(original_url)
        
        # Get the current path and query string
        query_string = request.META.get('QUERY_STRING', '')
        
        # If there's a query string, we need to reconstruct the full URL
        if query_string:
            full_path = f"{path}?{query_string}"
        else:
            full_path = path
        
        # Pattern to match customer codes at the end of URLs
        # Matches: /blog/2/NAE1495, /open-house/NAE1495, /facebook/https://facebook.com/page/NAE1495, etc.
        
        # First try social media pattern: /facebook/https://facebook.com/page/NAE1495
        # Updated to handle URLs with query parameters and mixed case customer codes
        social_media_pattern = r'^/(facebook|instagram|twitter|linkedin|telegram|youtube)/(.+)/u-([^/]+)/?$'
        match = re.match(social_media_pattern, full_path)
        
        if match:
            page_type, encoded_url, code_without_prefix = match.groups()
            # Decode the URL (handle both encoded and unencoded URLs)
            if '%' in encoded_url:
                # URL is encoded, decode it properly
                original_url = encoded_url.replace('%2F', '/').replace('%3A', ':').replace('%2E', '.').replace('%3F', '?').replace('%3D', '=')
            else:
                # URL is not encoded, use as is
                original_url = encoded_url
            page_id = None
        else:
            # Try pattern with page ID: /blog/2/u-NAE1495
            pattern_with_id = r'^/([^/]+)/([^/]+)/u-([^/]+)/?$'
            match = re.match(pattern_with_id, full_path)
            
            if match:
                page_type, page_id, code_without_prefix = match.groups()
                original_url = None
            else:
                # Try pattern without page ID: /open-house/u-NAE1495
                pattern_without_id = r'^/([^/]+)/u-([^/]+)/?$'
                match = re.match(pattern_without_id, full_path)
                
                if match:
                    page_type, code_without_prefix = match.groups()
                    page_id = None
                    original_url = None
                else:
                    # Try root pattern: /u-NAE1495
                    pattern_root = r'^/u-([^/]+)/?$'
                    match = re.match(pattern_root, full_path)
                    
                    if match:
                        code_without_prefix = match.groups()[0]
                        page_type = ''
                        page_id = None
                        original_url = None
                    else:
                        return None
        
        # Build full customer code with prefix
        if match:
            customer_code = f'u-{code_without_prefix}'
        
        if match:
            
            # Map URL patterns to our page types
            page_type_mapping = {
                'blog': 'blog',
                'buy-lease': 'buy',
                'selling': 'sell',
                'open-house': 'open_house',
                'mortgage-calculator': 'mortgage',
                'terms-of-service': 'terms',
                'privacy-policy': 'privacy',
                'cookie-policy': 'cookies',
                '': 'home',  # root path
            }
            
            # Get the mapped page type
            mapped_page_type = page_type_mapping.get(page_type, page_type)
            
            # Create the original URL (without tracking code)
            if original_url is not None:
                # Social media URL - already decoded
                pass
            elif page_type == 'blog':
                original_url = f"/blog/{page_id}/"
            elif page_type == 'buy-lease':
                original_url = "/buy-lease/"
            elif page_type == 'selling':
                original_url = "/selling/"
            elif page_type == 'open-house':
                original_url = "/open-house/"
            elif page_type == 'mortgage-calculator':
                original_url = "/mortgage-calculator/"
            elif page_type == '':  # Root pattern /NAE1495
                original_url = "/"
            else:
                original_url = f"/{page_type}/"
            
            # Get system information
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            referrer = request.META.get('HTTP_REFERER', '')
            language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0] if request.META.get('HTTP_ACCEPT_LANGUAGE') else ''
            
            # Get or create the tracking record
            tracking_record, created = LinkTracking.objects.get_or_create(
                customer_code=customer_code,
                page_type=mapped_page_type,
                page_id=page_id if page_type == 'blog' else None,
                defaults={
                    'original_url': original_url if original_url.startswith('http') else request.build_absolute_uri(original_url),
                    'tracked_url': request.build_absolute_uri(),
                }
            )
            
            # Record the click
            tracking_record.record_click(
                ip_address=ip_address,
                user_agent=user_agent,
                referrer=referrer,
                language=language
            )
            
            # Send tracking data to CRM webhook
            try:
                send_link_tracking_to_crm(tracking_record, request)
            except Exception as e:
                # Log error but don't break the redirect
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Failed to send link tracking to CRM: {str(e)}")
            
            # Redirect to the clean URL (without tracking code)
            return HttpResponseRedirect(original_url)

        return None
    
    def _get_platform_from_url(self, url):
        """Determine platform from URL"""
        url_lower = url.lower()
        
        if 'facebook.com' in url_lower:
            return 'facebook'
        elif 'instagram.com' in url_lower:
            return 'instagram'
        elif 'twitter.com' in url_lower or 'x.com' in url_lower:
            return 'twitter'
        elif 'linkedin.com' in url_lower:
            return 'linkedin'
        elif 't.me' in url_lower or 'telegram.me' in url_lower:
            return 'telegram'
        elif 'youtube.com' in url_lower or 'youtu.be' in url_lower:
            return 'youtube'
        else:
            return 'external'  # Generic external link
    
    def _get_internal_page_info(self, url, request):
        """Determine page type and ID from internal URL"""
        # Remove domain if present
        if url.startswith('http'):
            from urllib.parse import urlparse
            parsed = urlparse(url)
            path = parsed.path
        else:
            path = url
        
        # Remove leading slash
        path = path.lstrip('/')
        
        # Map URL patterns to page types
        if path.startswith('blog/'):
            # Extract blog post ID: /blog/2/ -> page_type='blog', page_id='2'
            parts = path.split('/')
            if len(parts) >= 2 and parts[1].isdigit():
                return 'blog', parts[1]
            else:
                return 'blog', None
        elif path.startswith('buy-lease/'):
            return 'buy', None
        elif path.startswith('selling/'):
            return 'sell', None
        elif path.startswith('open-house/'):
            return 'open_house', None
        elif path.startswith('mortgage-calculator/'):
            return 'mortgage', None
        elif path == '' or path == '/':
            return 'home', None
        else:
            # Generic internal page
            return 'internal', None
