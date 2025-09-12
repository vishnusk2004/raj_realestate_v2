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
    image_url = models.URLField(max_length=500, help_text="Main property image URL")
    additional_images = models.TextField(blank=True, help_text="Additional image URLs (one per line)")
    featured = models.BooleanField(default=False, help_text="Featured properties appear first")
    published = models.BooleanField(default=True, help_text="Only published properties are visible")
    contact_email = models.EmailField(help_text="Contact email for inquiries", default="abhi.gupta82@gmail.com")
    contact_phone = models.CharField(max_length=20, help_text="Contact phone number", default="+1 (315) 395-8315")
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


class BlogPost(models.Model):
    """Model to store blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default="Henry Oak Reality")
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description for blog listing")
    image_url = models.URLField(max_length=500, blank=True, help_text="Main image URL for the blog post")
    featured = models.BooleanField(default=False, help_text="Featured posts appear first")
    published = models.BooleanField(default=True, help_text="Only published posts are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
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
    image_url = models.URLField(max_length=500, help_text="Property image URL", default="https://via.placeholder.com/400x300")
    open_house_date = models.DateField(help_text="Date of the open house")
    open_house_time = models.TimeField(help_text="Time of the open house")
    contact_email = models.EmailField(help_text="Contact email for inquiries", default="abhi.gupta82@gmail.com")
    contact_phone = models.CharField(max_length=20, help_text="Contact phone number", default="+1 (315) 395-8315")
    published = models.BooleanField(default=True, help_text="Only published open houses are visible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['open_house_date', 'open_house_time']
        verbose_name = "Open House"
        verbose_name_plural = "Open Houses"
    
    def __str__(self):
        return f"{self.title} - {self.open_house_date} at {self.open_house_time}"
    
    @property
    def is_past(self):
        """Check if the open house date has passed"""
        from django.utils import timezone
        
        if not self.open_house_date:
            return False
            
        today = timezone.now().date()
        return self.open_house_date < today
