#!/usr/bin/env python
"""
Custom widgets for Django admin
"""
from django import forms
from django.utils.safestring import mark_safe

class RichTextWidget(forms.Textarea):
    """Custom widget for rich text editing with HTML support"""
    
    def __init__(self, attrs=None):
        default_attrs = {
            'rows': 20,
            'cols': 80,
            'class': 'rich-text-editor'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        
        # Add helpful HTML guide
        help_text = """
        <div style="margin-top: 10px; padding: 10px; background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 4px;">
            <h4 style="margin: 0 0 10px 0; color: #495057;">HTML Formatting Guide:</h4>
            <div style="font-size: 12px; line-height: 1.4;">
                <p><strong>Headers:</strong> &lt;h1&gt;Main Title&lt;/h1&gt;, &lt;h2&gt;Subtitle&lt;/h2&gt;, &lt;h3&gt;Section&lt;/h3&gt;</p>
                <p><strong>Text:</strong> &lt;p&gt;Paragraph&lt;/p&gt;, &lt;strong&gt;Bold&lt;/strong&gt;, &lt;em&gt;Italic&lt;/em&gt;</p>
                <p><strong>Lists:</strong> &lt;ul&gt;&lt;li&gt;Item 1&lt;/li&gt;&lt;li&gt;Item 2&lt;/li&gt;&lt;/ul&gt;</p>
                <p><strong>Tables:</strong> &lt;table&gt;&lt;tr&gt;&lt;td&gt;Cell&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;</p>
                <p><strong>Images:</strong> &lt;img src="url" alt="description" style="max-width: 100%;"&gt;</p>
                <p><strong>Links:</strong> &lt;a href="url"&gt;Link Text&lt;/a&gt;</p>
                <p><strong>Line breaks:</strong> &lt;br&gt;, &lt;hr&gt; (horizontal rule)</p>
            </div>
        </div>
        """
        
        return mark_safe(html + help_text)

class ColorPickerWidget(forms.TextInput):
    """Custom widget for color picker"""
    
    def __init__(self, attrs=None):
        default_attrs = {
            'type': 'color',
            'class': 'color-picker'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
