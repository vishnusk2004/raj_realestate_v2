#!/usr/bin/env python
"""
Custom forms for Django admin
"""
from django import forms
from .models import BlogPost, PropertyListing
from .widgets import RichTextWidget, ColorPickerWidget

class PropertyListingForm(forms.ModelForm):
    """Custom form for PropertyListing"""
    
    class Meta:
        model = PropertyListing
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    """Custom form for BlogPost with rich text editing"""
    
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': RichTextWidget(attrs={'rows': 20, 'cols': 80}),
            'text_color': ColorPickerWidget(),
            'background_color': ColorPickerWidget(),
            'font_family': forms.Select(choices=[
                ('Arial', 'Arial'),
                ('Georgia', 'Georgia'),
                ('Times New Roman', 'Times New Roman'),
                ('Helvetica', 'Helvetica'),
                ('Verdana', 'Verdana'),
                ('Courier New', 'Courier New'),
                ('Trebuchet MS', 'Trebuchet MS'),
                ('Arial Black', 'Arial Black'),
                ('Comic Sans MS', 'Comic Sans MS'),
                ('Impact', 'Impact'),
            ]),
            'font_size': forms.Select(choices=[
                ('12px', '12px (Small)'),
                ('14px', '14px (Regular)'),
                ('16px', '16px (Medium)'),
                ('18px', '18px (Large)'),
                ('20px', '20px (X-Large)'),
                ('24px', '24px (XX-Large)'),
                ('1.2em', '1.2em (Relative)'),
                ('1.4em', '1.4em (Relative)'),
                ('1.6em', '1.6em (Relative)'),
            ]),
            'line_height': forms.Select(choices=[
                ('1.2', '1.2 (Tight)'),
                ('1.4', '1.4 (Normal)'),
                ('1.6', '1.6 (Comfortable)'),
                ('1.8', '1.8 (Loose)'),
                ('2.0', '2.0 (Very Loose)'),
            ]),
        }