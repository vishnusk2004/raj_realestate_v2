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
    
    def get_additional_images_list(self):
        """Return list of additional image URLs"""
        if self.additional_images:
            return [url.strip() for url in self.additional_images.split('\n') if url.strip()]
        return []
    
    def get_main_image_url(self):
        """Return the main image URL - either from URL field or uploaded file"""
        if self.image_file:
            return self.image_file.url
        elif self.image_url:
            # Check if it's a data URL or regular URL
            if self.image_url.startswith('data:'):
                return self.image_url
            else:
                return self.image_url
        return None


class BlogPost(models.Model):
    """Model to store blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default="Henry Oak Reality")
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description for blog listing")
    image_url = models.URLField(max_length=500, blank=True, help_text="Main image URL for the blog post")
    image_file = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text="Upload an image file (alternative to image URL)")
    featured = models.BooleanField(default=False, help_text="Featured posts appear first")
    published = models.BooleanField(default=True, help_text="Only published posts are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def get_image_url(self):
        """Return the image URL, preferring uploaded file over URL"""
        if self.image_file:
            return self.image_file.url
        return self.image_url
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Create slug from title if not provided
            self.slug = self.title.lower().replace(' ', '-').replace('&', 'and')
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
    open_house_date = models.DateField(null=False, blank=False, help_text="Date of the open house")
    open_house_time = models.TimeField(help_text="Time of the open house")
    contact_email = models.EmailField(help_text="Contact email for inquiries", default="raj.gupta@kw.com")
    contact_phone = models.CharField(max_length=20, help_text="Contact phone number", default="(832) 785-0140")
    published = models.BooleanField(default=True, help_text="Only published open houses are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['open_house_date', 'open_house_time']
        verbose_name = "Open House"
    
    def get_main_image_url(self):
        """Return the main image URL, preferring uploaded file over URL"""
        if self.image_file:
            return self.image_file.url
        return self.image_url
    
    def __str__(self):
        date_str = self.open_house_date.strftime('%Y-%m-%d') if self.open_house_date else 'No Date'
        return f"{self.title} - {date_str}"
    
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
    caption = models.CharField(max_length=200, blank=True, help_text="Optional image caption")
    is_primary = models.BooleanField(default=False, help_text="Mark as primary image for the property")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (0 = first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Open House Image"
        verbose_name_plural = "Open House Images"
    
    def get_image_url(self):
        """Return the image URL, preferring uploaded file over URL"""
        if self.image_file:
            return self.image_file.url
        return self.image_url
    
    def __str__(self):
        return f"{self.open_house.title} - Image {self.order + 1}"


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
