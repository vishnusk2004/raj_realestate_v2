from django.contrib import admin
from django.conf import settings
from .models import Property, SellingContact, BlogTracking, BlogPost, PropertyListing, PropertyListingImage, OpenHouse, OpenHouseImage, OpenHouseRegistration, PropertyInquiry, MortgageInquiry, LinkTracking
from .forms import PropertyListingForm, BlogPostForm

# Configure admin site
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', 'Raj Real Estate Admin')
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', 'Raj Admin')
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', 'Raj Real Estate Administration')

# Inline admin classes
class PropertyListingImageInline(admin.TabularInline):
    model = PropertyListingImage
    extra = 1
    fields = ('image_file', 'image_url', 'caption', 'is_primary', 'order')
    ordering = ('order',)

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'bedrooms', 'bathrooms', 'area')
    list_filter = ('location', 'bedrooms', 'bathrooms')
    search_fields = ('title', 'location')

@admin.register(SellingContact)
class SellingContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_type', 'ip_address', 'created_at')
    list_filter = ('property_type', 'created_at', 'language')
    search_fields = ('name', 'email', 'phone', 'ip_address')
    readonly_fields = ('created_at', 'ip_address', 'user_agent', 'referrer', 'language')
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Property Details', {
            'fields': ('property_address', 'property_type', 'estimated_value', 'timeline', 'message')
        }),
        ('System Information', {
            'fields': ('ip_address', 'user_agent', 'referrer', 'language'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

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
    form = PropertyListingForm
    inlines = [PropertyListingImageInline]
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
        ('Main Image', {
            'fields': ('image_file', 'image_url'),
            'description': 'Main property image. You can either upload an image file or provide an image URL/data URL. If both are provided, the uploaded file will be used. Data URLs (base64) are supported for direct image embedding.'
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
    form = BlogPostForm
    list_display = ('title', 'author', 'category', 'featured', 'published', 'created_at')
    list_filter = ('category', 'featured', 'published', 'created_at', 'author')
    search_fields = ('title', 'content', 'author', 'category')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'content_preview')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category', 'excerpt')
        }),
        ('Content', {
            'fields': ('content', 'image_url', 'image_file', 'image_base64'),
            'description': 'Use HTML tags for rich formatting. Supported tags: &lt;h1&gt;-&lt;h6&gt;, &lt;p&gt;, &lt;strong&gt;, &lt;em&gt;, &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;, &lt;table&gt;, &lt;tr&gt;, &lt;td&gt;, &lt;th&gt;, &lt;img&gt;, &lt;br&gt;, &lt;hr&gt;, &lt;a&gt;. Use {{image_1}}, {{image_2}}, etc. to insert uploaded images anywhere in your content. Main image will be automatically converted to base64.'
        }),
        ('Content Images', {
            'fields': ('image_1', 'image_2', 'image_3', 'image_4', 'image_5'),
            'description': 'Upload images to use in your blog content. Reference them in your content using {{image_1}}, {{image_2}}, etc. Images will be automatically converted to base64 for storage.',
            'classes': ('collapse',)
        }),
        ('Base64 Image Data', {
            'fields': ('image_1_base64', 'image_2_base64', 'image_3_base64', 'image_4_base64', 'image_5_base64'),
            'description': 'Base64 encoded image data (automatically generated from uploaded images)',
            'classes': ('collapse',)
        }),
        ('Live Preview', {
            'fields': ('content_preview',),
            'description': 'This shows how your content will look with the formatting applied below.',
            'classes': ('collapse',)
        }),
        ('Text Formatting', {
            'fields': ('text_color', 'font_family', 'font_size', 'line_height'),
            'description': 'Customize the appearance of your blog post text'
        }),
        ('Settings', {
            'fields': ('featured', 'published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class OpenHouseImageInline(admin.TabularInline):
    model = OpenHouseImage
    extra = 1
    fields = ('image_file', 'image_url', 'caption', 'is_primary', 'order')
    ordering = ('order',)

@admin.register(OpenHouse)
class OpenHouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_address', 'price', 'open_house_date', 'open_house_time', 'published', 'is_past')
    list_filter = ('published', 'open_house_date', 'created_at')
    search_fields = ('title', 'property_address', 'description')
    readonly_fields = ('created_at', 'updated_at', 'is_past')
    inlines = [OpenHouseImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'property_address', 'price')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'area_sqft', 'description', 'features')
        }),
        ('Main Image', {
            'fields': ('image_file', 'image_url'),
            'description': 'Upload a main image file or provide an image URL'
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


@admin.register(OpenHouseRegistration)
class OpenHouseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'open_house', 'interested_in_buying', 'interested_in_leasing', 'created_at')
    list_filter = ('interested_in_buying', 'interested_in_leasing', 'preferred_contact_time', 'created_at', 'open_house')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Visitor Information', {
            'fields': ('name', 'email', 'phone', 'message')
        }),
        ('Open House', {
            'fields': ('open_house',)
        }),
        ('Interest Details', {
            'fields': ('interested_in_buying', 'interested_in_leasing', 'preferred_contact_time')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(PropertyInquiry)
class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_type', 'budget_range', 'location', 'ip_address', 'created_at')
    list_filter = ('property_type', 'budget_range', 'created_at', 'language')
    search_fields = ('name', 'email', 'phone', 'location', 'requirements', 'ip_address')
    readonly_fields = ('created_at', 'ip_address', 'user_agent', 'referrer', 'language')
    ordering = ('-created_at',)
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Property Preferences', {
            'fields': ('property_type', 'budget_range', 'location', 'requirements')
        }),
        ('System Information', {
            'fields': ('ip_address', 'user_agent', 'referrer', 'language'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(MortgageInquiry)
class MortgageInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_type', 'home_price', 'credit_score', 'ip_address', 'created_at')
    list_filter = ('property_type', 'credit_score', 'loan_term', 'created_at', 'language')
    search_fields = ('name', 'email', 'phone', 'additional_info', 'ip_address')
    readonly_fields = ('created_at', 'ip_address', 'user_agent', 'referrer', 'language')
    ordering = ('-created_at',)
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Property Details', {
            'fields': ('property_type', 'home_price', 'down_payment', 'loan_term')
        }),
        ('Financial Information', {
            'fields': ('credit_score', 'additional_info')
        }),
        ('System Information', {
            'fields': ('ip_address', 'user_agent', 'referrer', 'language'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(LinkTracking)
class LinkTrackingAdmin(admin.ModelAdmin):
    list_display = ('customer_code', 'page_type', 'page_id', 'click_count', 'first_clicked_at', 'last_clicked_at', 'ip_address')
    list_filter = ('page_type', 'first_clicked_at', 'last_clicked_at', 'created_at')
    search_fields = ('customer_code', 'customer_name', 'customer_email', 'ip_address')
    readonly_fields = ('created_at', 'updated_at', 'first_clicked_at', 'last_clicked_at', 'click_count', 'ip_address', 'user_agent', 'referrer', 'language')
    fieldsets = (
        ('Tracking Information', {
            'fields': ('customer_code', 'page_type', 'page_id', 'original_url', 'tracked_url')
        }),
        ('Customer Information', {
            'fields': ('customer_name', 'customer_email')
        }),
        ('Click Statistics', {
            'fields': ('click_count', 'first_clicked_at', 'last_clicked_at')
        }),
        ('System Information', {
            'fields': ('ip_address', 'user_agent', 'referrer', 'language'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(OpenHouseImage)
class OpenHouseImageAdmin(admin.ModelAdmin):
    list_display = ('open_house', 'caption', 'is_primary', 'order', 'created_at')
    list_filter = ('is_primary', 'created_at', 'open_house')
    search_fields = ('open_house__title', 'caption')
    ordering = ('open_house', 'order')
    fieldsets = (
        ('Image Information', {
            'fields': ('open_house', 'image_file', 'image_url', 'caption')
        }),
        ('Display Settings', {
            'fields': ('is_primary', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
