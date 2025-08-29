from django.db import models


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
