from django.contrib import admin
from .models import Property, SellingContact, BlogTracking

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
