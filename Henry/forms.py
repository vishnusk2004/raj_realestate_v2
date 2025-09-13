from django import forms
from .models import BlogPost, PropertyListing


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'excerpt', 'content', 'image_url', 'featured', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog post title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a brief excerpt'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Enter the full blog post content (HTML allowed)'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Title',
            'author': 'Author',
            'excerpt': 'Excerpt',
            'content': 'Content',
            'image_url': 'Image URL',
            'featured': 'Featured Post',
            'published': 'Published',
        }


class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['title', 'property_type', 'price', 'location', 'address', 'bedrooms', 'bathrooms', 
                 'parking_spaces', 'area_sqft', 'description', 'image_file', 'image_url', 
                 'additional_images', 'contact_email', 'contact_phone', 'featured', 'published']
        widgets = {
            'image_url': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Enter image URL or paste base64 data URL (data:image/...)',
                'style': 'font-family: monospace; font-size: 12px;'
            }),
        }