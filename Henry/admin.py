from django.contrib import admin
from .models import Property, SellingContact

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
