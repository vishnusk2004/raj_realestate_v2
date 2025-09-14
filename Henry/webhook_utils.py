import requests
import json
from datetime import datetime
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# CRM Webhook URL
CRM_WEBHOOK_URL = "https://workflow-automation.podio.com/catch/8g78a8102321zec"

def send_to_crm(form_type, lead_data, request=None):
    """
    Send form data to CRM webhook
    
    Args:
        form_type (str): Type of form (property_inquiry, mortgage_inquiry, etc.)
        lead_data (dict): Form data collected
        request: Django request object for additional context
    """
    try:
        # Prepare the payload
        payload = {
            "form_type": form_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "source_page": get_source_page(form_type),
            "lead_data": lead_data,
            "system_info": get_system_info(request) if request else {}
        }
        
        # Send to CRM
        response = requests.post(
            CRM_WEBHOOK_URL,
            json=payload,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Henry-Oak-Realty-Webhook/1.0'
            },
            timeout=10  # 10 second timeout
        )
        
        if response.status_code == 200:
            logger.info(f"Successfully sent {form_type} data to CRM")
            return True
        else:
            logger.error(f"CRM webhook failed with status {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending data to CRM: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error in webhook: {str(e)}")
        return False

def get_source_page(form_type):
    """Map form type to source page"""
    mapping = {
        'property_inquiry': 'buy-lease',
        'mortgage_inquiry': 'mortgage-calculator',
        'open_house_registration': 'open-house',
        'selling_contact': 'selling'
    }
    return mapping.get(form_type, 'unknown')

def get_system_info(request):
    """Extract system information from request"""
    if not request:
        return {}
    
    return {
        "user_agent": request.META.get('HTTP_USER_AGENT', ''),
        "ip_address": get_client_ip(request),
        "referrer": request.META.get('HTTP_REFERER', ''),
        "language": request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    }

def get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def format_property_inquiry_data(form_data):
    """Format property inquiry form data for CRM"""
    return {
        "contact_info": {
            "name": form_data.get('name', ''),
            "email": form_data.get('email', ''),
            "phone": form_data.get('phone', '')
        },
        "form_specific_data": {
            "property_type": form_data.get('property_type', ''),
            "budget_range": form_data.get('budget_range', ''),
            "location": form_data.get('location', ''),
            "timeline": form_data.get('timeline', ''),
            "financing_status": form_data.get('financing_status', '')
        },
        "property_interest": {
            "property_type": form_data.get('property_type', ''),
            "budget_range": form_data.get('budget_range', ''),
            "location": form_data.get('location', ''),
            "interested_in_buying": form_data.get('interested_in_buying') == 'on',
            "interested_in_leasing": form_data.get('interested_in_leasing') == 'on'
        },
        "preferences": {
            "preferred_contact_time": form_data.get('preferred_contact_time', ''),
            "message": form_data.get('message', '')
        }
    }

def format_mortgage_inquiry_data(form_data):
    """Format mortgage inquiry form data for CRM"""
    return {
        "contact_info": {
            "name": form_data.get('name', ''),
            "email": form_data.get('email', ''),
            "phone": form_data.get('phone', '')
        },
        "form_specific_data": {
            "property_type": form_data.get('property_type', ''),
            "home_price": form_data.get('home_price', ''),
            "down_payment": form_data.get('down_payment', ''),
            "loan_term": form_data.get('loan_term', ''),
            "interest_rate": form_data.get('interest_rate', ''),
            "calculated_payment": form_data.get('calculated_payment', '')
        },
        "property_interest": {
            "property_type": form_data.get('property_type', ''),
            "budget_range": f"${form_data.get('home_price', '0')}",
            "location": form_data.get('location', ''),
            "interested_in_buying": True,
            "interested_in_leasing": False
        },
        "preferences": {
            "preferred_contact_time": form_data.get('preferred_contact_time', ''),
            "message": form_data.get('message', '')
        }
    }

def format_open_house_data(form_data):
    """Format open house registration data for CRM"""
    return {
        "contact_info": {
            "name": form_data.get('name', ''),
            "email": form_data.get('email', ''),
            "phone": form_data.get('phone', '')
        },
        "form_specific_data": {
            "interested_in_buying": form_data.get('interested_in_buying') == 'on',
            "interested_in_leasing": form_data.get('interested_in_leasing') == 'on',
            "preferred_contact_time": form_data.get('preferred_contact_time', '')
        },
        "property_interest": {
            "property_type": "open_house",
            "budget_range": "",
            "location": "",
            "interested_in_buying": form_data.get('interested_in_buying') == 'on',
            "interested_in_leasing": form_data.get('interested_in_leasing') == 'on'
        },
        "preferences": {
            "preferred_contact_time": form_data.get('preferred_contact_time', ''),
            "message": form_data.get('message', '')
        }
    }

def format_selling_contact_data(form_data):
    """Format selling contact form data for CRM"""
    return {
        "contact_info": {
            "name": form_data.get('name', ''),
            "email": form_data.get('email', ''),
            "phone": form_data.get('phone', '')
        },
        "form_specific_data": {
            "property_address": form_data.get('property_address', ''),
            "property_type": form_data.get('property_type', ''),
            "bedrooms": form_data.get('bedrooms', ''),
            "bathrooms": form_data.get('bathrooms', ''),
            "square_footage": form_data.get('square_footage', ''),
            "estimated_value": form_data.get('estimated_value', ''),
            "timeline": form_data.get('timeline', '')
        },
        "property_interest": {
            "property_type": form_data.get('property_type', ''),
            "budget_range": f"${form_data.get('estimated_value', '0')}",
            "location": form_data.get('property_address', ''),
            "interested_in_buying": False,
            "interested_in_leasing": False
        },
        "preferences": {
            "preferred_contact_time": form_data.get('preferred_contact_time', ''),
            "message": form_data.get('message', '')
        }
    }
