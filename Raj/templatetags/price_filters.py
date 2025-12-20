from django import template
import json

register = template.Library()

@register.filter
def format_price(value):
    """Format price with commas"""
    try:
        return f"${int(value):,}"
    except (ValueError, TypeError):
        return value

@register.filter
def format_price_with_type(value, property_type):
    """Format price with commas and type-specific suffix"""
    try:
        formatted_price = f"${int(value):,}"
        if property_type == 'lease':
            return f"{formatted_price}/month"
        return formatted_price
    except (ValueError, TypeError):
        return value

@register.filter
def to_json(value):
    """Convert Python object to JSON string"""
    try:
        return json.dumps(value)
    except (TypeError, ValueError):
        return '[]'
