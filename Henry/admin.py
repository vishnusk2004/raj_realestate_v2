from django.contrib import admin
from .models import Property, SellingContact, BlogTracking, BlogPost, PropertyListing, OpenHouse

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'bedrooms', 'bathrooms', 'area')
    list_filter = ('location', 'bedrooms', 'bathrooms')
    search_fields = ('title', 'location')

@admin.register(SellingContact)
class SellingContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_type', 'created_at')
    list_filter = ('property_type', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)

@admin.register(BlogTracking)
class BlogTrackingAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_email', 'blog_post_id', 'is_opened', 'created_at', 'opened_at')
    list_filter = ('is_opened', 'blog_post_id', 'created_at')
    search_fields = ('member_name', 'member_email', 'tracking_code', 'crm_reference')
    readonly_fields = ('tracking_code', 'created_at', 'opened_at', 'ip_address', 'user_agent')
    fieldsets = (
        ('Member Information', {
            'fields': ('member_name', 'member_email', 'member_phone', 'crm_reference')
        }),
        ('Blog Post', {
            'fields': ('blog_post_id',)
        }),
        ('Tracking Information', {
            'fields': ('tracking_code', 'is_opened', 'created_at', 'opened_at', 'ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('member_name', 'member_email', 'member_phone', 'blog_post_id', 'crm_reference')
        return self.readonly_fields


@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'location', 'bedrooms', 'bathrooms', 'featured', 'published', 'created_at')
    list_filter = ('property_type', 'featured', 'published', 'bedrooms', 'bathrooms', 'created_at')
    search_fields = ('title', 'location', 'address', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'property_type', 'price', 'location', 'address')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'parking_spaces', 'area_sqft', 'description')
        }),
        ('Images', {
            'fields': ('image_file', 'image_url', 'additional_images'),
            'description': 'You can either upload an image file or provide an image URL. If both are provided, the uploaded file will be used.'
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Settings', {
            'fields': ('featured', 'published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'featured', 'published', 'created_at')
    list_filter = ('featured', 'published', 'created_at', 'author')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'excerpt')
        }),
        ('Content', {
            'fields': ('content', 'image_url')
        }),
        ('Settings', {
            'fields': ('featured', 'published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(OpenHouse)
class OpenHouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_address', 'price', 'open_house_date', 'open_house_time', 'published', 'is_past')
    list_filter = ('published', 'open_house_date', 'created_at')
    search_fields = ('title', 'property_address', 'description')
    readonly_fields = ('created_at', 'updated_at', 'is_past')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'property_address', 'price')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'area_sqft', 'description', 'image_url')
        }),
        ('Open House Details', {
            'fields': ('open_house_date', 'open_house_time')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Settings', {
            'fields': ('published',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'is_past'),
            'classes': ('collapse',)
        }),
    )