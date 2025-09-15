from django.contrib import admin
from .models import Property, SellingContact, BlogTracking, BlogPost, PropertyListing, OpenHouse, OpenHouseRegistration, PropertyInquiry, MortgageInquiry, LinkTracking
from .forms import PropertyListingForm

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
            'description': 'You can either upload an image file or provide an image URL/data URL. If both are provided, the uploaded file will be used. Data URLs (base64) are supported for direct image embedding.'
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
            'fields': ('content', 'image_url', 'image_file')
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
    ) 
 @ a d m i n . r e g i s t e r ( L i n k T r a c k i n g )  
 c l a s s   L i n k T r a c k i n g A d m i n ( a d m i n . M o d e l A d m i n ) :  
         l i s t _ d i s p l a y   =   ( ' c u s t o m e r _ c o d e ' ,   ' p a g e _ t y p e ' ,   ' p a g e _ i d ' ,   ' c l i c k _ c o u n t ' ,   ' f i r s t _ c l i c k e d _ a t ' ,   ' l a s t _ c l i c k e d _ a t ' ,   ' i p _ a d d r e s s ' )  
         l i s t _ f i l t e r   =   ( ' p a g e _ t y p e ' ,   ' f i r s t _ c l i c k e d _ a t ' ,   ' l a s t _ c l i c k e d _ a t ' ,   ' c r e a t e d _ a t ' )  
         s e a r c h _ f i e l d s   =   ( ' c u s t o m e r _ c o d e ' ,   ' c u s t o m e r _ n a m e ' ,   ' c u s t o m e r _ e m a i l ' ,   ' i p _ a d d r e s s ' )  
         r e a d o n l y _ f i e l d s   =   ( ' c r e a t e d _ a t ' ,   ' u p d a t e d _ a t ' ,   ' f i r s t _ c l i c k e d _ a t ' ,   ' l a s t _ c l i c k e d _ a t ' ,   ' c l i c k _ c o u n t ' ,   ' i p _ a d d r e s s ' ,   ' u s e r _ a g e n t ' ,   ' r e f e r r e r ' ,   ' l a n g u a g e ' )  
         f i e l d s e t s   =   (  
                 ( ' T r a c k i n g   I n f o r m a t i o n ' ,   {  
                         ' f i e l d s ' :   ( ' c u s t o m e r _ c o d e ' ,   ' p a g e _ t y p e ' ,   ' p a g e _ i d ' ,   ' o r i g i n a l _ u r l ' ,   ' t r a c k e d _ u r l ' )  
                 } ) ,  
                 ( ' C u s t o m e r   I n f o r m a t i o n ' ,   {  
                         ' f i e l d s ' :   ( ' c u s t o m e r _ n a m e ' ,   ' c u s t o m e r _ e m a i l ' )  
                 } ) ,  
                 ( ' C l i c k   S t a t i s t i c s ' ,   {  
                         ' f i e l d s ' :   ( ' c l i c k _ c o u n t ' ,   ' f i r s t _ c l i c k e d _ a t ' ,   ' l a s t _ c l i c k e d _ a t ' )  
                 } ) ,  
                 ( ' S y s t e m   I n f o r m a t i o n ' ,   {  
                         ' f i e l d s ' :   ( ' i p _ a d d r e s s ' ,   ' u s e r _ a g e n t ' ,   ' r e f e r r e r ' ,   ' l a n g u a g e ' ) ,  
                         ' c l a s s e s ' :   ( ' c o l l a p s e ' , )  
                 } ) ,  
                 ( ' T i m e s t a m p s ' ,   {  
                         ' f i e l d s ' :   ( ' c r e a t e d _ a t ' ,   ' u p d a t e d _ a t ' ) ,  
                         ' c l a s s e s ' :   ( ' c o l l a p s e ' , )  
                 } ) ,  
         )  
 