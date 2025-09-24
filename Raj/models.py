from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Property(models.Model):
    title = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    parking_space = models.IntegerField(null=True)
    area = models.CharField(max_length=50)
    site_url = models.URLField(null=True, max_length=255)
    image_url = models.URLField(null=True, max_length=255)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class SellingContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    property_address = models.TextField(blank=True, null=True)
    property_type = models.CharField(max_length=50, blank=True, null=True)
    estimated_value = models.CharField(max_length=50, blank=True, null=True)
    timeline = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # System tracking fields
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the submitter")
    user_agent = models.TextField(blank=True, null=True, help_text="Browser/device information")
    referrer = models.URLField(blank=True, null=True, help_text="Page that referred the user")
    language = models.CharField(max_length=50, blank=True, null=True, help_text="User's preferred language")
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class BlogTracking(models.Model):
    """Model to track blog post opens with unique codes"""
    tracking_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    blog_post_id = models.IntegerField(help_text="ID of the blog post being tracked")
    member_name = models.CharField(max_length=200, help_text="Name of the member receiving the link")
    member_email = models.EmailField(help_text="Email of the member receiving the link")
    member_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number of the member")
    crm_reference = models.CharField(max_length=100, blank=True, null=True, help_text="Reference from CRM system")
    created_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True, help_text="When the link was first opened")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the opener")
    user_agent = models.TextField(blank=True, null=True, help_text="Browser/device information")
    is_opened = models.BooleanField(default=False, help_text="Whether the link has been opened")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Tracking"
        verbose_name_plural = "Blog Trackings"
    
    def __str__(self):
        return f"{self.member_name} - {self.tracking_code} - {'Opened' if self.is_opened else 'Not Opened'}"
    
    def mark_as_opened(self, ip_address=None, user_agent=None):
        """Mark this tracking record as opened"""
        if not self.is_opened:
            self.is_opened = True
            self.opened_at = timezone.now()
            if ip_address:
                self.ip_address = ip_address
            if user_agent:
                self.user_agent = user_agent
            self.save()


class LinkTracking(models.Model):
    """Model to track all types of link clicks with customer codes"""
    PAGE_TYPES = [
        ('blog', 'Blog Post'),
        ('buy', 'Buy/Lease Page'),
        ('sell', 'Selling Page'),
        ('open_house', 'Open House'),
        ('mortgage', 'Mortgage Calculator'),
        ('home', 'Home Page'),
        ('contact', 'Contact Page'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('telegram', 'Telegram'),
        ('youtube', 'YouTube'),
    ]
    
    customer_code = models.CharField(max_length=100, help_text="Unique customer code (e.g., NAE1495)")
    page_type = models.CharField(max_length=20, choices=PAGE_TYPES, help_text="Type of page being tracked")
    page_id = models.CharField(max_length=100, blank=True, null=True, help_text="ID of the specific page (e.g., blog post ID)")
    original_url = models.URLField(help_text="The original URL without tracking code")
    tracked_url = models.URLField(help_text="The URL with tracking code")
    
    # Customer information
    customer_name = models.CharField(max_length=200, blank=True, null=True, help_text="Customer name if available")
    customer_email = models.EmailField(blank=True, null=True, help_text="Customer email if available")
    
    # Tracking data
    first_clicked_at = models.DateTimeField(null=True, blank=True, help_text="When the link was first clicked")
    last_clicked_at = models.DateTimeField(null=True, blank=True, help_text="When the link was last clicked")
    click_count = models.IntegerField(default=0, help_text="Total number of clicks")
    
    # System information
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the clicker")
    user_agent = models.TextField(blank=True, null=True, help_text="Browser/device information")
    referrer = models.URLField(blank=True, null=True, help_text="Page that referred the user")
    language = models.CharField(max_length=50, blank=True, null=True, help_text="User's preferred language")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['customer_code', 'page_type', 'page_id']
        ordering = ['-last_clicked_at', '-created_at']
        verbose_name = "Link Tracking"
        verbose_name_plural = "Link Trackings"
    
    def __str__(self):
        return f"{self.customer_code} - {self.get_page_type_display()} - {self.click_count} clicks"
    
    def record_click(self, ip_address=None, user_agent=None, referrer=None, language=None):
        """Record a click on this tracked link"""
        now = timezone.now()
        
        # Set first click time if this is the first click
        if not self.first_clicked_at:
            self.first_clicked_at = now
        
        # Update last click time and increment count
        self.last_clicked_at = now
        self.click_count += 1
        
        # Update system information
        if ip_address:
            self.ip_address = ip_address
        if user_agent:
            self.user_agent = user_agent
        if referrer:
            self.referrer = referrer
        if language:
            self.language = language
            
            self.save()


class PropertyListing(models.Model):
    """Model to store property listings for Buy/Lease section"""
    PROPERTY_TYPE_CHOICES = [
        ('buy', 'For Sale'),
        ('lease', 'For Lease'),
    ]
    
    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES, default='buy')
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Price in dollars")
    location = models.CharField(max_length=200)
    address = models.TextField(help_text="Full property address")
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    parking_spaces = models.IntegerField(null=True, blank=True)
    area_sqft = models.IntegerField(null=True, blank=True, help_text="Area in square feet")
    description = models.TextField(help_text="Detailed property description")
    image_url = models.TextField(blank=True, help_text="Main property image URL or base64 data URL (optional if uploading file)")
    image_file = models.ImageField(upload_to='properties/', blank=True, null=True, help_text="Upload property image (optional if providing URL)")
    image_base64 = models.TextField(blank=True, null=True, help_text="Base64 encoded image data")
    additional_images = models.TextField(blank=True, help_text="Additional image URLs (one per line)")
    featured = models.BooleanField(default=False, help_text="Featured properties appear first")
    published = models.BooleanField(default=True, help_text="Only published properties are visible")
    contact_email = models.EmailField(help_text="Contact email for inquiries", default="raj.gupta@kw.com")
    contact_phone = models.CharField(max_length=20, help_text="Contact phone number", default="(832) 785-0140")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = "Property Listing"
        verbose_name_plural = "Property Listings"
    
    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()}"
    
    def save(self, *args, **kwargs):
        """Override save to automatically convert uploaded images to base64"""
        # Convert uploaded file to base64 if present and no base64 exists
        if self.image_file and self.image_file.name and not self.image_base64:
            from .image_utils import image_to_base64
            self.image_base64 = image_to_base64(self.image_file)
        
        super().save(*args, **kwargs)
    
    def get_additional_images_list(self):
        """Return list of additional image URLs"""
        if self.additional_images:
            return [url.strip() for url in self.additional_images.split('\n') if url.strip()]
        return []
    
    def get_all_image_urls(self):
        """Return list of all image URLs (main + additional + related images) - prioritize base64"""
        image_urls = []
        
        # Add main image - prioritize base64
        if self.image_base64:
            image_urls.append(self.image_base64)
        elif self.image_file and self.image_file.name:
            # Convert file to base64 if not already done
            try:
                from .image_utils import image_to_base64
                base64_data = image_to_base64(self.image_file)
                if base64_data:
                    image_urls.append(base64_data)
            except:
                pass
        elif self.image_url:
            image_urls.append(self.image_url)
        
        # Add related images - prioritize base64
        for img in self.images.all():
            if img.image_base64:
                image_urls.append(img.image_base64)
            elif img.image_file and img.image_file.name:
                # Convert file to base64 if not already done
                try:
                    from .image_utils import image_to_base64
                    base64_data = image_to_base64(img.image_file)
                    if base64_data:
                        image_urls.append(base64_data)
                except:
                    pass
            elif img.image_url:
                image_urls.append(img.image_url)
        
        # Add additional images from text field (these should already be base64 or URLs)
        additional_urls = self.get_additional_images_list()
        image_urls.extend(additional_urls)
        
        return image_urls
    
    def get_main_image_url(self):
        """Return the main image URL - prefer base64, then file, then URL"""
        # First priority: base64 data
        if self.image_base64:
            from .image_utils import get_image_data_url
            return get_image_data_url(self.image_base64)
        
        # Second priority: uploaded file
        if self.image_file and self.image_file.name:
            # In production, if the file exists but might not be accessible,
            # fall back to the image_url if available
            try:
                # Check if we're in production (no DEBUG mode)
                from django.conf import settings
                if not settings.DEBUG and self.image_url:
                    return self.image_url
                return self.image_file.url
            except:
                # If there's any error accessing the file, fall back to URL
                if self.image_url:
                    return self.image_url
                return self.image_file.url
        
        # Third priority: URL field
        elif self.image_url:
            # Check if it's a data URL or regular URL
            if self.image_url.startswith('data:'):
                return self.image_url
            else:
                return self.image_url
        
        return None


class BlogPostImage(models.Model):
    """Model to store multiple images for blog posts"""
    blog_post = models.ForeignKey('BlogPost', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/gallery/')
    caption = models.CharField(max_length=200, blank=True, help_text='Optional caption for the image')
    order = models.PositiveIntegerField(default=0, help_text='Order of display')
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Blog Post Image"
        verbose_name_plural = "Blog Post Images"
    
    def __str__(self):
        return f"{self.blog_post.title} - Image {self.order}"
    
    def get_image_url(self):
        """Return the image URL"""
        if self.image:
            return self.image.url
        return None


class BlogPost(models.Model):
    """Model to store blog posts with rich text content"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default="Henry Oak Reality")
    content = models.TextField(help_text="Rich text content with HTML formatting. Use {{image_1}}, {{image_2}}, etc. to insert uploaded images anywhere in your content.")
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description for blog listing")
    image_url = models.URLField(max_length=500, blank=True, help_text="Main image URL for the blog post")
    image_file = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text="Upload an image file (alternative to image URL)")
    image_base64 = models.TextField(blank=True, null=True, help_text="Base64 encoded main image data")
    
    # Additional images for content (base64 storage)
    image_1_base64 = models.TextField(blank=True, null=True, help_text="Content image 1 (base64) - use {{image_1}} in content")
    image_2_base64 = models.TextField(blank=True, null=True, help_text="Content image 2 (base64) - use {{image_2}} in content")
    image_3_base64 = models.TextField(blank=True, null=True, help_text="Content image 3 (base64) - use {{image_3}} in content")
    image_4_base64 = models.TextField(blank=True, null=True, help_text="Content image 4 (base64) - use {{image_4}} in content")
    image_5_base64 = models.TextField(blank=True, null=True, help_text="Content image 5 (base64) - use {{image_5}} in content")
    
    # Keep original ImageField for admin upload (will be converted to base64)
    image_1 = models.ImageField(upload_to='blog_images/content/', blank=True, null=True, help_text="Content image 1 - will be converted to base64")
    image_2 = models.ImageField(upload_to='blog_images/content/', blank=True, null=True, help_text="Content image 2 - will be converted to base64")
    image_3 = models.ImageField(upload_to='blog_images/content/', blank=True, null=True, help_text="Content image 3 - will be converted to base64")
    image_4 = models.ImageField(upload_to='blog_images/content/', blank=True, null=True, help_text="Content image 4 - will be converted to base64")
    image_5 = models.ImageField(upload_to='blog_images/content/', blank=True, null=True, help_text="Content image 5 - will be converted to base64")
    
    # Rich text formatting options
    text_color = models.CharField(max_length=7, default="#000000", help_text="Text color (hex code, e.g., #000000)")
    font_family = models.CharField(max_length=50, default="Arial", help_text="Font family (e.g., Arial, Georgia, Times New Roman)")
    font_size = models.CharField(max_length=10, default="16px", help_text="Font size (e.g., 16px, 1.2em)")
    line_height = models.CharField(max_length=10, default="1.6", help_text="Line height (e.g., 1.6, 24px)")
    
    CATEGORY_CHOICES = [
        ('buying_guide', 'Buying Guide'),
        ('selling_tips', 'Selling Tips'),
        ('market_analysis', 'Market Analysis'),
        ('investment', 'Investment'),
        ('finance', 'Finance'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='buying_guide', help_text="Blog post category")
    featured = models.BooleanField(default=False, help_text="Featured posts appear first")
    published = models.BooleanField(default=True, help_text="Only published posts are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def get_image_url(self):
        """Return the image URL - prefer base64, then file, then URL"""
        # First priority: base64 data
        if self.image_base64:
            from .image_utils import get_image_data_url
            return get_image_data_url(self.image_base64)
        
        # Second priority: uploaded file
        if self.image_file and self.image_file.name:
            return self.image_file.url
        
        # Third priority: URL
        return self.image_url
    
    def __str__(self):
        return self.title
    
    def get_formatted_content(self):
        """Return content with applied formatting styles and image placeholders replaced"""
        if not self.content:
            return ""
        
        # Process content to replace image placeholders
        processed_content = self.process_image_placeholders(self.content)
        
        # Sanitize HTML to prevent conflicts
        sanitized_content = self.sanitize_html(processed_content)
        
        # Create style attributes
        style_parts = [
            f"color: {self.text_color}",
            f"font-family: {self.font_family}",
            f"font-size: {self.font_size}",
            f"line-height: {self.line_height}",
        ]
        
        style_attr = "; ".join(style_parts)
        
        # Wrap content in isolated container with scoped styles
        return f'''
        <div class="blog-content-isolated" style="{style_attr}">
            <style scoped>
                .blog-content-isolated * {{
                    box-sizing: border-box;
                }}
                .blog-content-isolated h1, .blog-content-isolated h2, .blog-content-isolated h3, 
                .blog-content-isolated h4, .blog-content-isolated h5, .blog-content-isolated h6 {{
                    margin-top: 1.5em;
                    margin-bottom: 0.5em;
                    font-weight: 600;
                }}
                .blog-content-isolated h1 {{ font-size: 2.25rem; line-height: 1.2; }}
                .blog-content-isolated h2 {{ font-size: 1.875rem; line-height: 1.3; }}
                .blog-content-isolated h3 {{ font-size: 1.5rem; line-height: 1.4; }}
                .blog-content-isolated h4 {{ font-size: 1.25rem; line-height: 1.4; }}
                .blog-content-isolated h5 {{ font-size: 1.125rem; line-height: 1.4; }}
                .blog-content-isolated h6 {{ font-size: 1rem; line-height: 1.4; }}
                .blog-content-isolated p {{
                    margin-bottom: 1em;
                }}
                .blog-content-isolated ul, .blog-content-isolated ol {{
                    margin-bottom: 1em;
                    padding-left: 2em;
                }}
                .blog-content-isolated li {{
                    margin-bottom: 0.5em;
                }}
                .blog-content-isolated blockquote {{
                    border-left: 4px solid #e5e7eb;
                    padding-left: 1em;
                    margin: 1em 0;
                    font-style: italic;
                }}
                .blog-content-isolated code {{
                    background-color: #f3f4f6;
                    padding: 0.2em 0.4em;
                    border-radius: 0.25rem;
                    font-family: monospace;
                }}
                .blog-content-isolated pre {{
                    background-color: #f3f4f6;
                    padding: 1em;
                    border-radius: 0.5rem;
                    overflow-x: auto;
                    margin: 1em 0;
                }}
                .blog-content-isolated img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 0.5rem;
                    margin: 1em 0;
                }}
                .blog-content-isolated a {{
                    color: #3b82f6;
                    text-decoration: underline;
                }}
                .blog-content-isolated a:hover {{
                    color: #1d4ed8;
                }}
                .blog-content-isolated table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 1em 0;
                }}
                .blog-content-isolated th, .blog-content-isolated td {{
                    border: 1px solid #e5e7eb;
                    padding: 0.5em;
                    text-align: left;
                }}
                .blog-content-isolated th {{
                    background-color: #f9fafb;
                    font-weight: 600;
                }}
            </style>
            {sanitized_content}
        </div>
        '''
    
    def process_image_placeholders(self, content):
        """Replace {{image_1}}, {{image_2}}, etc. with actual image HTML using base64 data"""
        import re
        
        # Dictionary of base64 image fields
        image_fields = {
            'image_1': self.image_1_base64,
            'image_2': self.image_2_base64,
            'image_3': self.image_3_base64,
            'image_4': self.image_4_base64,
            'image_5': self.image_5_base64,
        }
        
        processed_content = content
        
        # Replace each image placeholder
        for field_name, base64_data in image_fields.items():
            if base64_data and base64_data.strip():
                # Create image HTML with responsive styling using base64 data
                image_html = f'''
                <div style="text-align: center; margin: 20px 0;">
                    <img src="{base64_data}" 
                         alt="Blog content image" 
                         style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                </div>
                '''
                # Replace the placeholder with the image HTML
                processed_content = processed_content.replace(f'{{{{{field_name}}}}}', image_html)
            else:
                # Remove placeholder if no image is uploaded
                processed_content = processed_content.replace(f'{{{{{field_name}}}}}', '')
        
        return processed_content
    
    def sanitize_html(self, content):
        """Sanitize HTML content to prevent conflicts with page styling and security issues"""
        from bs4 import BeautifulSoup, NavigableString
        import re
        
        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Define allowed tags and their attributes
        allowed_tags = {
            'p': ['class', 'style'],
            'h1': ['class', 'style'],
            'h2': ['class', 'style'],
            'h3': ['class', 'style'],
            'h4': ['class', 'style'],
            'h5': ['class', 'style'],
            'h6': ['class', 'style'],
            'div': ['class', 'style'],
            'span': ['class', 'style'],
            'strong': [],
            'b': [],
            'em': [],
            'i': [],
            'u': [],
            'br': [],
            'hr': [],
            'ul': ['class', 'style'],
            'ol': ['class', 'style'],
            'li': ['class', 'style'],
            'blockquote': ['class', 'style'],
            'code': ['class', 'style'],
            'pre': ['class', 'style'],
            'a': ['href', 'target', 'rel', 'class', 'style'],
            'img': ['src', 'alt', 'width', 'height', 'class', 'style'],
            'table': ['class', 'style'],
            'thead': ['class', 'style'],
            'tbody': ['class', 'style'],
            'tr': ['class', 'style'],
            'th': ['class', 'style', 'colspan', 'rowspan'],
            'td': ['class', 'style', 'colspan', 'rowspan'],
        }
        
        # Remove dangerous tags and attributes
        for tag in soup.find_all():
            # Remove script, style, iframe, object, embed, form, input, button tags
            if tag.name in ['script', 'style', 'iframe', 'object', 'embed', 'form', 'input', 'button', 'link', 'meta']:
                tag.decompose()
                continue
            
            # Remove dangerous attributes
            dangerous_attrs = ['onclick', 'onload', 'onerror', 'onmouseover', 'onfocus', 'onblur', 'onchange', 'onsubmit']
            for attr in dangerous_attrs:
                if attr in tag.attrs:
                    del tag.attrs[attr]
            
            # Remove javascript: and dangerous data: URLs from href and src
            if 'href' in tag.attrs:
                href = tag.attrs['href']
                if href.startswith(('javascript:', 'data:text/html', 'data:application', 'vbscript:')):
                    tag.attrs['href'] = '#'
                else:
                    # Add security attributes for external links
                    if href.startswith(('http://', 'https://')):
                        tag.attrs['rel'] = 'noopener noreferrer'
                        tag.attrs['target'] = '_blank'
            
            if 'src' in tag.attrs:
                src = tag.attrs['src']
                # Allow data:image URLs for base64 images, but block other data: URLs
                if src.startswith(('javascript:', 'data:text/html', 'data:application', 'vbscript:')):
                    tag.attrs['src'] = ''
                # Keep data:image URLs for base64 images
            
            # Remove any attributes not in the allowed list
            if tag.name in allowed_tags:
                allowed_attrs = allowed_tags[tag.name]
                attrs_to_remove = []
                for attr in tag.attrs:
                    if attr not in allowed_attrs:
                        attrs_to_remove.append(attr)
                for attr in attrs_to_remove:
                    del tag.attrs[attr]
            else:
                # If tag is not allowed, replace with its text content
                tag.unwrap()
        
        # Clean up any remaining dangerous content
        content_str = str(soup)
        
        # Remove any remaining script tags or dangerous patterns
        dangerous_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:',
            r'data:text/html',
            r'vbscript:',
            r'on\w+\s*=',
        ]
        
        for pattern in dangerous_patterns:
            content_str = re.sub(pattern, '', content_str, flags=re.IGNORECASE | re.DOTALL)
        
        return content_str
    
    def get_content_style(self):
        """Return CSS style string for the content"""
        style_parts = [
            f"color: {self.text_color}",
            f"font-family: {self.font_family}",
            f"font-size: {self.font_size}",
            f"line-height: {self.line_height}",
        ]
        
        return "; ".join(style_parts)
    
    def content_preview(self):
        """Return formatted content for admin preview with actual images"""
        if not self.content:
            return "No content to preview"
        
        # Process content to replace image placeholders with actual images
        processed_content = self.process_image_placeholders(self.content)
        
        # Create style attributes
        style_parts = [
            f"color: {self.text_color}",
            f"font-family: {self.font_family}",
            f"font-size: {self.font_size}",
            f"line-height: {self.line_height}",
        ]
        style_attr = "; ".join(style_parts)
        
        # Wrap content in styled div
        formatted_content = f'<div style="{style_attr}">{processed_content}</div>'
        
        # Add some basic CSS for better preview
        preview_html = f"""
        <div style="
            border: 1px solid #ddd; 
            padding: 20px; 
            margin: 10px 0; 
            background: #f9f9f9; 
            border-radius: 5px;
            max-height: 400px; 
            overflow-y: auto;
        ">
            <h4 style="margin-top: 0; color: #666;">Preview:</h4>
            <div style="
                background: white; 
                padding: 15px; 
                border-radius: 3px; 
                border: 1px solid #eee;
            ">
                {formatted_content}
            </div>
        </div>
        """
        return preview_html
    
    content_preview.allow_tags = True
    content_preview.short_description = "Content Preview"
    
    def convert_image_to_base64(self, image_field):
        """Convert uploaded image to base64 data URL"""
        if image_field and image_field.name:
            try:
                from PIL import Image
                import base64
                import io
                
                # Open and process the image
                img = Image.open(image_field)
                
                # Convert to RGB if necessary (for PNG with transparency)
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Resize if too large (max 1200px width)
                if img.width > 1200:
                    ratio = 1200 / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((1200, new_height), Image.Resampling.LANCZOS)
                
                # Convert to base64
                buffer = io.BytesIO()
                img.save(buffer, format='JPEG', quality=85, optimize=True)
                img_data = buffer.getvalue()
                base64_data = base64.b64encode(img_data).decode('utf-8')
                
                return f"data:image/jpeg;base64,{base64_data}"
            except Exception as e:
                print(f"Error converting image to base64: {e}")
                return None
        return None
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Create slug from title if not provided
            self.slug = self.title.lower().replace(' ', '-').replace('&', 'and')
            # Ensure slug is unique
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        
        # Convert main image to base64 if present and no base64 exists
        if self.image_file and self.image_file.name and not self.image_base64:
            from .image_utils import image_to_base64
            self.image_base64 = image_to_base64(self.image_file)
        
        # Convert uploaded images to base64
        if self.image_1 and not self.image_1_base64:
            self.image_1_base64 = self.convert_image_to_base64(self.image_1)
        if self.image_2 and not self.image_2_base64:
            self.image_2_base64 = self.convert_image_to_base64(self.image_2)
        if self.image_3 and not self.image_3_base64:
            self.image_3_base64 = self.convert_image_to_base64(self.image_3)
        if self.image_4 and not self.image_4_base64:
            self.image_4_base64 = self.convert_image_to_base64(self.image_4)
        if self.image_5 and not self.image_5_base64:
            self.image_5_base64 = self.convert_image_to_base64(self.image_5)
        
        super().save(*args, **kwargs)


class PropertyListingImage(models.Model):
    """Model to store multiple images for property listings"""
    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='properties/gallery/', help_text="Upload property image")
    image_url = models.URLField(max_length=500, blank=True, help_text="Alternative: Property image URL")
    image_base64 = models.TextField(blank=True, null=True, help_text="Base64 encoded image data")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional image caption")
    is_primary = models.BooleanField(default=False, help_text="Mark as primary image for the property")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (0 = first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Property Listing Image"
        verbose_name_plural = "Property Listing Images"
    
    def get_image_url(self):
        """Return the image URL - prefer base64, then file, then URL"""
        # First priority: base64 data
        if self.image_base64:
            return self.image_base64
        
        # Second priority: uploaded file - convert to base64
        if self.image_file and self.image_file.name:
            try:
                from .image_utils import image_to_base64
                base64_data = image_to_base64(self.image_file)
                if base64_data:
                    # Store the base64 data for future use
                    self.image_base64 = base64_data
                    self.save(update_fields=['image_base64'])
                    return base64_data
            except:
                pass
        
        # Third priority: URL field
        return self.image_url or ''
    
    def __str__(self):
        return f"{self.property_listing.title} - Image {self.order + 1}"
    
    def save(self, *args, **kwargs):
        """Override save to automatically convert uploaded images to base64"""
        # Convert uploaded file to base64 if present and no base64 exists
        if self.image_file and self.image_file.name and not self.image_base64:
            from .image_utils import image_to_base64
            self.image_base64 = image_to_base64(self.image_file)
        
        super().save(*args, **kwargs)


class OpenHouse(models.Model):
    """Model to store open house events"""
    title = models.CharField(max_length=200, help_text="Property title for open house", default="Property")
    property_address = models.TextField(help_text="Full property address", default="Address TBD")
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Property price in dollars", default=0.00)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    area_sqft = models.IntegerField(null=True, blank=True, help_text="Area in square feet")
    description = models.TextField(help_text="Property description", default="Property description")
    image_url = models.URLField(max_length=500, help_text="Property image URL", default="https://via.placeholder.com/400x300", blank=True)
    image_file = models.ImageField(upload_to='openhouse_images/', blank=True, null=True, help_text="Upload a main image file (alternative to image URL)")
    image_base64 = models.TextField(blank=True, null=True, help_text="Base64 encoded image data")
    open_house_date = models.DateField(null=False, blank=False, help_text="Date of the open house")
    open_house_time = models.TimeField(help_text="Time of the open house")
    contact_email = models.EmailField(help_text="Contact email for inquiries", default="raj.gupta@kw.com")
    contact_phone = models.CharField(max_length=20, help_text="Contact phone number", default="(832) 785-0140")
    features = models.TextField(blank=True, help_text="Property features (one per line, e.g., Updated Kitchen, Hardwood Floors, Large Backyard)")
    published = models.BooleanField(default=True, help_text="Only published open houses are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['open_house_date', 'open_house_time']
        verbose_name = "Open House"
    
    def __str__(self):
        date_str = self.open_house_date.strftime('%Y-%m-%d') if self.open_house_date else 'No Date'
        return f"{self.title} - {date_str}"
    
    def get_main_image_url(self):
        """Return the main image URL - prefer base64, then file, then URL"""
        # First priority: base64 data
        if self.image_base64:
            from .image_utils import get_image_data_url
            return get_image_data_url(self.image_base64)
        
        # Second priority: uploaded file
        if self.image_file and self.image_file.name:
            # In production, if the file exists but might not be accessible,
            # fall back to the image_url if available
            try:
                # Check if we're in production (no DEBUG mode)
                from django.conf import settings
                if not settings.DEBUG and self.image_url:
                    return self.image_url
                return self.image_file.url
            except:
                # If there's any error accessing the file, fall back to URL
                if self.image_url:
                    return self.image_url
                return self.image_file.url
        
        # Third priority: URL field
        elif self.image_url:
            # Check if it's a data URL or regular URL
            if self.image_url.startswith('data:'):
                return self.image_url
            else:
                return self.image_url
        
        return None
    
    def save(self, *args, **kwargs):
        """Override save to automatically convert uploaded images to base64"""
        # Convert uploaded file to base64 if present and no base64 exists
        if self.image_file and self.image_file.name and not self.image_base64:
            from .image_utils import image_to_base64
            self.image_base64 = image_to_base64(self.image_file)
        
        super().save(*args, **kwargs)
    
    def get_features_list(self):
        """Return list of property features"""
        if self.features:
            return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
        return []
    
    @property
    def is_past(self):
        """Check if the open house date has passed"""
        from django.utils import timezone
        if self.open_house_date is None:
            return False
        return self.open_house_date < timezone.now().date()


class OpenHouseImage(models.Model):
    """Model to store multiple images for open house properties"""
    open_house = models.ForeignKey(OpenHouse, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='openhouse_images/gallery/', help_text="Upload property image")
    image_url = models.URLField(max_length=500, blank=True, help_text="Alternative: Property image URL")
    image_base64 = models.TextField(blank=True, null=True, help_text="Base64 encoded image data")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional image caption")
    is_primary = models.BooleanField(default=False, help_text="Mark as primary image for the property")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (0 = first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Open House Image"
        verbose_name_plural = "Open House Images"
    
    def get_image_url(self):
        """Return the image URL - prefer base64, then file, then URL"""
        # First priority: base64 data
        if self.image_base64:
            from .image_utils import get_image_data_url
            return get_image_data_url(self.image_base64)
        
        # Second priority: uploaded file
        if self.image_file and self.image_file.name:
            # In production, if the file exists but might not be accessible,
            # fall back to the image_url if available
            try:
                # Check if we're in production (no DEBUG mode)
                from django.conf import settings
                if not settings.DEBUG and self.image_url:
                    return self.image_url
                return self.image_file.url
            except:
                # If there's any error accessing the file, fall back to URL
                if self.image_url:
                    return self.image_url
                return self.image_file.url
        
        # Third priority: URL field
        return self.image_url
    
    def __str__(self):
        return f"{self.open_house.title} - Image {self.order + 1}"
    
    def save(self, *args, **kwargs):
        """Override save to automatically convert uploaded images to base64"""
        # Convert uploaded file to base64 if present and no base64 exists
        if self.image_file and self.image_file.name and not self.image_base64:
            from .image_utils import image_to_base64
            self.image_base64 = image_to_base64(self.image_file)
        
        super().save(*args, **kwargs)


class OpenHouseRegistration(models.Model):
    """Model to store open house visitor registrations"""
    open_house = models.ForeignKey(OpenHouse, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100, help_text="Visitor's full name")
    email = models.EmailField(help_text="Visitor's email address")
    phone = models.CharField(max_length=20, help_text="Visitor's phone number")
    message = models.TextField(blank=True, null=True, help_text="Additional message or questions")
    interested_in_buying = models.BooleanField(default=False, help_text="Is the visitor interested in buying?")
    interested_in_leasing = models.BooleanField(default=False, help_text="Is the visitor interested in leasing?")
    preferred_contact_time = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        choices=[
            ('morning', 'Morning (9 AM - 12 PM)'),
            ('afternoon', 'Afternoon (12 PM - 5 PM)'),
            ('evening', 'Evening (5 PM - 8 PM)'),
            ('anytime', 'Anytime'),
        ],
        help_text="Preferred time to be contacted"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Open House Registration"
        verbose_name_plural = "Open House Registrations"
    
    def __str__(self):
        return f"{self.name} - {self.open_house.title} ({self.created_at.strftime('%Y-%m-%d')})"


class PropertyInquiry(models.Model):
    """Model to store property inquiry requests from buy-lease page"""
    name = models.CharField(max_length=100, help_text="Inquirer's full name")
    email = models.EmailField(help_text="Inquirer's email address")
    phone = models.CharField(max_length=20, help_text="Inquirer's phone number")
    property_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('house', 'House'),
            ('apartment', 'Apartment'),
            ('condo', 'Condo'),
            ('townhouse', 'Townhouse'),
            ('commercial', 'Commercial'),
        ],
        help_text="Type of property they're looking for"
    )
    budget_range = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('under-300k', 'Under $300,000'),
            ('300k-500k', '$300,000 - $500,000'),
            ('500k-750k', '$500,000 - $750,000'),
            ('750k-1m', '$750,000 - $1,000,000'),
            ('over-1m', 'Over $1,000,000'),
        ],
        help_text="Budget range for the property"
    )
    location = models.CharField(max_length=200, blank=True, null=True, help_text="Preferred location")
    requirements = models.TextField(blank=True, null=True, help_text="Specific requirements and preferences")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # System tracking fields
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the submitter")
    user_agent = models.TextField(blank=True, null=True, help_text="Browser/device information")
    referrer = models.URLField(blank=True, null=True, help_text="Page that referred the user")
    language = models.CharField(max_length=50, blank=True, null=True, help_text="User's preferred language")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Property Inquiry"
        verbose_name_plural = "Property Inquiries"

    def __str__(self):
        return f"{self.name} - {self.property_type or 'Any'} - {self.created_at.strftime('%Y-%m-%d')}"


class MortgageInquiry(models.Model):
    """Model to store mortgage inquiry requests from mortgage calculator page"""
    name = models.CharField(max_length=100, help_text="Inquirer's full name")
    email = models.EmailField(help_text="Inquirer's email address")
    phone = models.CharField(max_length=20, help_text="Inquirer's phone number")
    property_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('house', 'House'),
            ('apartment', 'Apartment'),
            ('condo', 'Condo'),
            ('townhouse', 'Townhouse'),
            ('commercial', 'Commercial'),
        ],
        help_text="Type of property they're interested in"
    )
    home_price = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        help_text="Home price they're considering"
    )
    down_payment = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        help_text="Down payment amount they have"
    )
    loan_term = models.IntegerField(
        blank=True,
        null=True,
        choices=[
            (15, '15 Years'),
            (20, '20 Years'),
            (25, '25 Years'),
            (30, '30 Years'),
        ],
        help_text="Preferred loan term in years"
    )
    credit_score = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ('excellent', 'Excellent (750+)'),
            ('good', 'Good (700-749)'),
            ('fair', 'Fair (650-699)'),
            ('poor', 'Poor (Below 650)'),
        ],
        help_text="Credit score range"
    )
    additional_info = models.TextField(blank=True, null=True, help_text="Additional information about their mortgage needs")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # System tracking fields
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the submitter")
    user_agent = models.TextField(blank=True, null=True, help_text="Browser/device information")
    referrer = models.URLField(blank=True, null=True, help_text="Page that referred the user")
    language = models.CharField(max_length=50, blank=True, null=True, help_text="User's preferred language")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mortgage Inquiry"
        verbose_name_plural = "Mortgage Inquiries"

    def __str__(self):
        return f"{self.name} - ${self.home_price or 'TBD'} - {self.created_at.strftime('%Y-%m-%d')}"
    
    @property
    def is_past(self):
        """Check if the open house date has passed"""
        from django.utils import timezone
        
        if not self.open_house_date:
            return False
            
        today = timezone.now().date()
        return self.open_house_date < today
