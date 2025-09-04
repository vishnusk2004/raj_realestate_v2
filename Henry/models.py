from django.db import models
import uuid
from django.utils import timezone


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
