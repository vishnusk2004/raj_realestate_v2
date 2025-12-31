from ast import literal_eval
from datetime import date

from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from .models import BlogTracking, BlogPost, PropertyListing, OpenHouse, OpenHouseRegistration, PropertyInquiry, MortgageInquiry, LinkTracking, Community
from .forms import BlogPostForm
import uuid
import json
import requests

from .models import Property, SellingContact


# Create your views here.

def send_podium_webhook(tracking_data):
    """
    Send tracking data to Podium webhook
    """
    try:
        podium_url = "https://workflow-automation.podio.com/catch/sajz0io9683p7b0"
        
        payload = {
            "event": "blog_link_opened",
            "tracking_code": tracking_data.get('tracking_code'),
            "member_name": tracking_data.get('member_name'),
            "member_phone": tracking_data.get('member_phone'),
            "member_email": tracking_data.get('member_email'),
            "blog_post_id": tracking_data.get('blog_post_id'),
            "crm_reference": tracking_data.get('crm_reference'),
            "opened_at": tracking_data.get('opened_at'),
            "ip_address": tracking_data.get('ip_address'),
            "user_agent": tracking_data.get('user_agent')
        }
        
        response = requests.post(podium_url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Failed to send Podium webhook: {str(e)}")
        return False

def home(request):
    try:
        # Debug: Print BRAND_NAME to console
        print(f"DEBUG: BRAND_NAME from settings = '{settings.BRAND_NAME}'")
        print(f"DEBUG: BRAND_NAME type = {type(settings.BRAND_NAME)}")
        print(f"DEBUG: BRAND_NAME repr = {repr(settings.BRAND_NAME)}")
        
        # Check for tracking code
        customer_code = request.GET.get('code')
        if customer_code:
            # Handle tracking
            from .webhook_utils import get_client_ip, send_link_tracking_to_crm
            
            # Get system information
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            referrer = request.META.get('HTTP_REFERER', '')
            language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0][:50] if request.META.get('HTTP_ACCEPT_LANGUAGE') else ''
            
            # Create or update tracking record
            tracking_record, created = LinkTracking.objects.get_or_create(
                customer_code=customer_code,
                page_type='home',
                page_id=None,
                defaults={
                    'original_url': '/',
                    'tracked_url': request.build_absolute_uri(),
                }
            )
            
            tracking_record.record_click(
                ip_address=ip_address,
                user_agent=user_agent,
                referrer=referrer,
                language=language
            )
            
            # Send to CRM
            try:
                send_link_tracking_to_crm(tracking_record, request)
            except Exception as e:
                print(f"Failed to send link tracking to CRM: {str(e)}")
        
        featured_properties = Property.objects.all()[:8]  # Get the first 8 properties or however many you want to display

        # Update each property's image_url to only contain the first URL
        for featured_property in featured_properties:
            try:
                # Use literal_eval to convert the string representation of the list into an actual list
                image_list = literal_eval(featured_property.image_url)
                # Assign only the first URL (if it exists)
                featured_property.cover_image_url = image_list[0] if image_list else None
            except (ValueError, SyntaxError):
                featured_property.cover_image_url = None  # Handle cases where image_url format is unexpected

        # Get Just Sold properties (12+ properties for show more)
        just_sold_properties = PropertyListing.objects.filter(
            published=True,
            property_status='just_sold'
        ).order_by('-created_at')
        
        # Get Just Leased properties (12+ properties for show more) - using 'for_lease' status for now
        just_leased_properties = PropertyListing.objects.filter(
            published=True,
            property_status='for_lease'
        ).order_by('-created_at')

        # Get featured communities
        featured_communities = Community.objects.filter(
            featured=True,
            published=True
        ).order_by('name')[:6]

        # Pass the updated queryset as context
        # Debug: Print BRAND_NAME to console
        print(f"DEBUG: BRAND_NAME from settings = '{settings.BRAND_NAME}'")
        print(f"DEBUG: BRAND_NAME type = {type(settings.BRAND_NAME)}")
        print(f"DEBUG: BRAND_NAME repr = {repr(settings.BRAND_NAME)}")
        
        context = {
            'featured_properties': featured_properties,
            'just_sold_properties': just_sold_properties,
            'just_leased_properties': just_leased_properties,
            'featured_communities': featured_communities,
            'brand_name': settings.BRAND_NAME
        }
        # Debug: Print what we're passing to template
        print(f"DEBUG: Passing brand_name to template = '{context['brand_name']}'")
        return render(request, 'Raj/index.html', context)
    except Exception as e:
        # Return a simple error response for debugging
        return HttpResponse(f"Error in home view: {str(e)}", status=500)


def featured_properties(request):
    properties = Property.objects.all()

    # Update each property's image_url to only contain the first URL
    for property in properties:
        try:
            # Convert the string representation of the list into an actual list
            image_list = literal_eval(property.image_url)
            property.cover_image_url = image_list[0] if image_list else None
        except (ValueError, SyntaxError):
            property.cover_image_url = None

    # Serialize the queryset to JSON format
    properties_json = mark_safe(serialize('json', properties))

    context = {
        'properties': properties,
        'properties_json': properties_json,  # Pass serialized JSON data
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/featured_properties.html', context)


def blog(request):
    """Blog page view with category filtering"""
    try:
        # Get filter parameters
        category = request.GET.get('category', '')
        search_query = request.GET.get('search', '')
        
        # Start with published blog posts
        posts = BlogPost.objects.filter(published=True)
        
        # Filter by category
        if category and category != 'all':
            posts = posts.filter(category=category)
        
        # Filter by search query
        if search_query:
            posts = posts.filter(
                models.Q(title__icontains=search_query) |
                models.Q(content__icontains=search_query) |
                models.Q(excerpt__icontains=search_query)
            )
        
        # Order by creation date (newest first)
        posts = posts.order_by('-created_at')
        
        context = {
            'posts': posts,
            'current_category': category,
            'search_query': search_query,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Raj/blog.html', context)
    except Exception as e:
        print(f"Error in blog view: {e}")
        return render(request, 'Raj/blog.html', {'posts': [], 'brand_name': settings.BRAND_NAME})


def blog_detail(request, post_id):
    """Blog detail page view with optional tracking"""
    try:
        # Check for tracking code
        customer_code = request.GET.get('code')
        if customer_code:
            # Handle tracking
            from .webhook_utils import get_client_ip, send_link_tracking_to_crm
            
            # Get system information
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            referrer = request.META.get('HTTP_REFERER', '')
            language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0][:50] if request.META.get('HTTP_ACCEPT_LANGUAGE') else ''
            
            # Create or update tracking record
            tracking_record, created = LinkTracking.objects.get_or_create(
                customer_code=customer_code,
                page_type='blog',
                page_id=str(post_id),
                defaults={
                    'original_url': f'/blog/{post_id}/',
                    'tracked_url': request.build_absolute_uri(),
                }
            )
            
            tracking_record.record_click(
                ip_address=ip_address,
                user_agent=user_agent,
                referrer=referrer,
                language=language
            )
            
            # Send to CRM
            try:
                send_link_tracking_to_crm(tracking_record, request)
            except Exception as e:
                print(f"Failed to send link tracking to CRM: {str(e)}")
        
        # Get the specific blog post from database
        post = get_object_or_404(BlogPost, id=post_id, published=True)
        
        # Get related posts (exclude current post, limit to 2)
        related_posts = BlogPost.objects.filter(published=True).exclude(id=post_id).order_by('-featured', '-created_at')[:2]
        
        context = {
            'post': post,
            'related_posts': related_posts,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Raj/blog_detail.html', context)
    except Exception as e:
        print(f"Error in blog_detail view: {e}")
        return HttpResponse("Blog post not found", status=404)


def blog_page(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/blog_page.html', context)


def buying(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/buying.html', context)


def selling(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            property_address = request.POST.get('property_address', '')
            property_type = request.POST.get('property_type', '')
            estimated_value = request.POST.get('estimated_value', '')
            timeline = request.POST.get('timeline', '')
            message = request.POST.get('message', '')
            
            # Validate required fields
            if not all([name, email, phone]):
                messages.error(request, 'Please fill in all required fields (Name, Email, and Phone Number).')
                return redirect('selling')
            
            # Get system info
            from .webhook_utils import get_system_info
            system_info = get_system_info(request)
            
            # Create and save the contact
            contact = SellingContact.objects.create(
                name=name,
                email=email,
                phone=phone,
                property_address=property_address,
                property_type=property_type,
                estimated_value=estimated_value,
                timeline=timeline,
                message=message,
                ip_address=system_info.get('ip_address'),
                user_agent=system_info.get('user_agent'),
                referrer=system_info.get('referrer'),
                language=system_info.get('language')
            )
            
            # Send to CRM via webhook
            from .webhook_utils import send_to_crm, format_selling_contact_data
            form_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'property_address': property_address,
                'property_type': property_type,
                'estimated_value': estimated_value,
                'timeline': timeline,
                'message': message,
                'preferred_contact_time': request.POST.get('preferred_contact_time', '')
            }
            lead_data = format_selling_contact_data(form_data)
            send_to_crm('selling_contact', lead_data, request)
            
            messages.success(request, 'Thank you! Our team will contact you within 24 hours.')
            return redirect('selling')
            
        except Exception as e:
            messages.error(request, 'There was an error submitting your request. Please try again.')
    
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/selling.html', context)


def leasing(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/leasing.html', context)


def home_valuation(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            property_type = request.POST.get('property_type')
            message = request.POST.get('message')
            
            # Create a simple contact record (you can create a model for this if needed)
            # For now, we'll just show success message
            messages.success(request, 'Your home valuation request has been submitted successfully! We will contact you within 24 hours.')
            return redirect('home_valuation')  # Redirect to clear the POST data
            
        except Exception as e:
            messages.error(request, 'There was an error submitting your request. Please try again.')
    
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/home_valuation.html', context)


def open_house(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message', '')
            property_type = request.POST.get('property_type', '')
            budget_range = request.POST.get('budget_range', '')
            preferred_date = request.POST.get('preferred_date', '')
            preferred_time = request.POST.get('preferred_time', '')
            open_house_id = request.POST.get('open_house_id')
            
            # Validate required fields
            if not all([name, email, phone, open_house_id]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('open_house')
            
            # Get the selected open house
            open_house_obj = get_object_or_404(OpenHouse, id=open_house_id, published=True)
            
            # Create the registration
            registration = OpenHouseRegistration.objects.create(
                open_house=open_house_obj,
                name=name,
                email=email,
                phone=phone,
                message=f"Property Type: {property_type}\nBudget Range: {budget_range}\nPreferred Date: {preferred_date}\nPreferred Time: {preferred_time}\n\nAdditional Information: {message}",
                interested_in_buying=True,  # Default to True since they're interested in open houses
                interested_in_leasing=False,
                preferred_contact_time=preferred_time.lower() if preferred_time else 'anytime'
            )
            
            # Send to CRM via webhook
            from .webhook_utils import send_to_crm, format_open_house_data
            form_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'property_type': property_type,
                'budget_range': budget_range,
                'preferred_date': preferred_date,
                'preferred_time': preferred_time,
                'open_house_id': open_house_id,
                'open_house_title': open_house_obj.title,
                'open_house_address': open_house_obj.property_address,
                'open_house_price': str(open_house_obj.price),
                'interested_in_buying': True,
                'interested_in_leasing': False,
                'preferred_contact_time': preferred_time.lower() if preferred_time else 'anytime'
            }
            lead_data = format_open_house_data(form_data)
            send_to_crm('open_house_registration', lead_data, request)
            
            messages.success(request, f'Thank you for registering for "{open_house_obj.title}"! We will contact you within 24 hours.')
            return redirect('open_house')  # Redirect to clear the POST data
            
        except Exception as e:
            messages.error(request, f'There was an error submitting your registration. Please try again. Error: {str(e)}')
    
    # Get all published open house events with related images
    open_houses = OpenHouse.objects.filter(published=True).prefetch_related('images').order_by('open_house_date', 'open_house_time')
    
    context = {
        'brand_name': settings.BRAND_NAME,
        'open_houses': open_houses
    }
    return render(request, 'Raj/open_house.html', context)


def mortgage_calculator(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/mortgage_calculator.html', context)


def market_insights(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/market_insights.html', context)


def tracked_blog_detail(request, tracking_code):
    """View to handle tracked blog links and record opens"""
    try:
        # Get the tracking record
        tracking = get_object_or_404(BlogTracking, tracking_code=tracking_code)
        
        # Mark as opened if not already opened
        if not tracking.is_opened:
            # Get client IP and user agent
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            tracking.mark_as_opened(ip_address=ip_address, user_agent=user_agent)
            
            # Send real-time notification to Podium webhook
            webhook_data = {
                'tracking_code': str(tracking.tracking_code),
                'member_name': tracking.member_name,
                'member_phone': tracking.member_phone,
                'member_email': tracking.member_email,
                'blog_post_id': tracking.blog_post_id,
                'crm_reference': tracking.crm_reference,
                'opened_at': tracking.opened_at.isoformat() if tracking.opened_at else None,
                'ip_address': ip_address,
                'user_agent': user_agent
            }
            send_podium_webhook(webhook_data)
        
        # Get the blog post from database
        post = get_object_or_404(BlogPost, id=tracking.blog_post_id, published=True)
        
        # Get related posts (exclude current post, limit to 2)
        related_posts = BlogPost.objects.filter(published=True).exclude(id=tracking.blog_post_id).order_by('-featured', '-created_at')[:2]
        
        context = {
            'post': post,
            'related_posts': related_posts,
            'tracking': tracking,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Raj/blog_detail.html', context)
        
    except Exception as e:
        return HttpResponse(f"Error in tracked blog view: {str(e)}", status=500)


@csrf_exempt
def create_tracking_link(request):
    """
    API endpoint to create tracking links for CRM integration
    
    Expected POST data:
    {
        "blog_post_id": 1,                    # Required: Which blog post to track
        "member_phone": "123-456-7890",       # Optional: Member's phone number
        "member_email": "john@example.com",   # Optional: Member's email
        "member_name": "John Doe",            # Optional: Member's name
        "crm_reference": "CRM-001"            # Optional: CRM reference
    }
    
    Note: At least one of member_phone or member_email must be provided
    
    Returns:
    {
        "success": true,
        "tracking_code": "uuid-here",
        "tracking_url": "http://yoursite.com/tracked-blog/uuid-here/",
        "member_phone": "123-456-7890",
        "member_email": "john@example.com",
        "member_name": "John Doe",
        "blog_post_id": 1,
        "crm_reference": "CRM-001"
    }
    """
    if request.method == 'POST':
        try:
            # Handle both form data and JSON data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            # Validate required fields
            blog_post_id = data.get('blog_post_id')
            if not blog_post_id:
                return JsonResponse({
                    'success': False,
                    'error': 'blog_post_id is required'
                }, status=400)
            
            try:
                blog_post_id = int(blog_post_id)
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'error': 'blog_post_id must be a valid integer'
                }, status=400)
            
            member_phone = data.get('member_phone', '').strip()
            member_email = data.get('member_email', '').strip()
            member_name = data.get('member_name', '').strip()
            crm_reference = data.get('crm_reference', '').strip()
            
            # At least one contact method must be provided
            if not member_phone and not member_email:
                return JsonResponse({
                    'success': False,
                    'error': 'At least one of member_phone or member_email must be provided'
                }, status=400)
            
            # Create tracking record
            tracking = BlogTracking.objects.create(
                blog_post_id=blog_post_id,
                member_name=member_name or 'Unknown',
                member_email=member_email,
                member_phone=member_phone,
                crm_reference=crm_reference
            )
            
            # Generate the new tracking URL format
            # Use customer_code (crm_reference) if available, otherwise use tracking_code
            customer_code = crm_reference or str(tracking.tracking_code)
            tracking_url = request.build_absolute_uri(f'/blog/{blog_post_id}/{customer_code}/')
            
            return JsonResponse({
                'success': True,
                'tracking_code': str(tracking.tracking_code),
                'tracking_url': tracking_url,
                'member_phone': member_phone,
                'member_email': member_email,
                'member_name': member_name,
                'blog_post_id': blog_post_id,
                'crm_reference': crm_reference
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST requests allowed'
    }, status=405)


def tracking_dashboard(request):
    """Admin dashboard to view tracking statistics"""
    if not request.user.is_staff:
        return HttpResponse("Access denied", status=403)
    
    # Get tracking statistics
    total_trackings = BlogTracking.objects.count()
    opened_trackings = BlogTracking.objects.filter(is_opened=True).count()
    unopened_trackings = total_trackings - opened_trackings
    
    # Get recent trackings
    recent_trackings = BlogTracking.objects.all()[:10]
    
    # Get statistics by blog post
    blog_stats = {}
    for tracking in BlogTracking.objects.all():
        post_id = tracking.blog_post_id
        if post_id not in blog_stats:
            blog_stats[post_id] = {'total': 0, 'opened': 0}
        blog_stats[post_id]['total'] += 1
        if tracking.is_opened:
            blog_stats[post_id]['opened'] += 1
    
    context = {
        'total_trackings': total_trackings,
        'opened_trackings': opened_trackings,
        'unopened_trackings': unopened_trackings,
        'open_rate': (opened_trackings / total_trackings * 100) if total_trackings > 0 else 0,
        'recent_trackings': recent_trackings,
        'blog_stats': blog_stats,
        'brand_name': settings.BRAND_NAME
    }
    
    return render(request, 'Raj/tracking_dashboard.html', context)


# Blog Admin Views
def blog_admin(request):
    """Blog admin dashboard"""
    posts = BlogPost.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/blog_admin.html', context)


def blog_add(request):
    """Add new blog post"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_admin')
    else:
        form = BlogPostForm()
    
    context = {
        'form': form,
        'title': 'Add New Blog Post',
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/blog_form.html', context)


def blog_edit(request, post_id):
    """Edit existing blog post"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog_admin')
    else:
        form = BlogPostForm(instance=post)
    
    context = {
        'form': form,
        'title': f'Edit: {post.title}',
        'post': post,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/blog_form.html', context)


def blog_delete(request, post_id):
    """Delete blog post"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog_admin')
    
    context = {
        'post': post,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/blog_delete.html', context)


def buy_lease(request):
    """Buy/Lease properties page"""
    # Get filter parameters
    property_type = request.GET.get('property_type', '')
    search_query = request.GET.get('search', '')
    price_range = request.GET.get('price_range', '')
    property_id = request.GET.get('property_id', '')
    
    # Start with published properties and include related images and videos
    properties = PropertyListing.objects.filter(published=True).prefetch_related('images', 'videos')
    
    # Filter by property type
    if property_type in ['buy', 'lease']:
        properties = properties.filter(property_type=property_type)
    
    # Filter by search query
    if search_query:
        properties = properties.filter(
            models.Q(title__icontains=search_query) |
            models.Q(location__icontains=search_query) |
            models.Q(address__icontains=search_query) |
            models.Q(description__icontains=search_query)
        )
    
    # Filter by price range
    if price_range:
        try:
            min_price, max_price = price_range.split('-')
            min_price = int(min_price)
            max_price = int(max_price)
            properties = properties.filter(price__gte=min_price, price__lte=max_price)
        except (ValueError, AttributeError):
            pass  # Invalid price range, ignore filter
    
    # Order by featured first, then by creation date
    properties = properties.order_by('-featured', '-created_at')
    
    context = {
        'properties': properties,
        'current_type': property_type,
        'search_query': search_query,
        'price_range': price_range,
        'property_id': property_id,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/buy_lease.html', context)


def debug_images(request):
    """Debug page to test property images"""
    properties = PropertyListing.objects.filter(published=True).prefetch_related('images')
    context = {
        'properties': properties,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/debug_images.html', context)

def debug_blog_image(request, post_id):
    """Debug page to test blog post images"""
    post = get_object_or_404(BlogPost, id=post_id)
    context = {
        'post': post,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/debug_blog_image.html', context)


def debug_open_house_images(request, open_house_id):
    """Debug page to test open house images"""
    open_house = get_object_or_404(OpenHouse, id=open_house_id)
    context = {
        'open_house': open_house,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/debug_open_house_images.html', context)


def community_detail(request, slug):
    """Community detail page showing all properties in that community"""
    community = get_object_or_404(Community, slug=slug, published=True)
    
    # Get filter parameters
    property_type = request.GET.get('property_type', '')
    property_status = request.GET.get('property_status', '')
    search_query = request.GET.get('search', '')
    
    # Start with properties in this community
    properties = PropertyListing.objects.filter(
        community=community,
        published=True
    ).prefetch_related('images', 'videos')
    
    # Filter by property type
    if property_type in ['buy', 'lease']:
        properties = properties.filter(property_type=property_type)
    
    # Filter by property status
    if property_status:
        properties = properties.filter(property_status=property_status)
    
    # Filter by search query
    if search_query:
        properties = properties.filter(
            models.Q(title__icontains=search_query) |
            models.Q(location__icontains=search_query) |
            models.Q(address__icontains=search_query) |
            models.Q(description__icontains=search_query)
        )
    
    # Order by featured first, then by creation date
    properties = properties.order_by('-featured', '-created_at')
    
    context = {
        'community': community,
        'properties': properties,
        'brand_name': settings.BRAND_NAME,
        'property_type_filter': property_type,
        'property_status_filter': property_status,
        'search_query': search_query,
    }
    
    return render(request, 'Raj/community_detail.html', context)


def property_inquiry(request):
    """Handle property inquiry form submissions from buy-lease page"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            property_type = request.POST.get('property_type', '')
            budget_range = request.POST.get('budget_range', '')
            location = request.POST.get('location', '')
            requirements = request.POST.get('requirements', '')
            
            # Validate required fields
            if not all([name, email, phone]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('buy_lease')
            
            # Get system info
            from .webhook_utils import get_client_ip, get_system_info
            system_info = get_system_info(request)
            
            # Create the inquiry with safety truncation
            inquiry = PropertyInquiry.objects.create(
                name=name[:100] if name else None,  # Truncate to 100 chars
                email=email,
                phone=phone[:20] if phone else None,  # Truncate to 20 chars
                property_type=property_type[:50] if property_type else None,  # Truncate to 50 chars
                budget_range=budget_range[:50] if budget_range else None,  # Truncate to 50 chars
                location=location[:200] if location else None,  # Truncate to 200 chars
                requirements=requirements if requirements else None,  # TextField, no truncation needed
                ip_address=system_info.get('ip_address'),
                user_agent=system_info.get('user_agent'),  # TextField, no truncation needed
                referrer=system_info.get('referrer'),
                language=system_info.get('language')[:50] if system_info.get('language') else None  # Truncate to 50 chars
            )
            
            # Send to CRM via webhook
            from .webhook_utils import send_to_crm, format_property_inquiry_data
            form_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'property_type': property_type,
                'budget_range': budget_range,
                'location': location,
                'message': requirements,
                'interested_in_buying': request.POST.get('interested_in_buying', ''),
                'interested_in_leasing': request.POST.get('interested_in_leasing', ''),
                'preferred_contact_time': request.POST.get('preferred_contact_time', '')
            }
            lead_data = format_property_inquiry_data(form_data)
            send_to_crm('property_inquiry', lead_data, request)
            
            messages.success(request, f'Thank you for your inquiry, {name}! Our team will contact you within 24 hours to help you find the perfect property.')
            return redirect('buy_lease')
            
        except Exception as e:
            messages.error(request, f'There was an error submitting your inquiry. Please try again. Error: {str(e)}')
            return redirect('buy_lease')
    
    # If not POST, redirect to buy_lease page
    return redirect('buy_lease')


def mortgage_inquiry(request):
    """Handle mortgage inquiry form submissions from mortgage calculator page"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            property_type = request.POST.get('property_type', '')
            home_price = request.POST.get('home_price', '')
            down_payment = request.POST.get('down_payment', '')
            loan_term = request.POST.get('loan_term', '')
            credit_score = request.POST.get('credit_score', '')
            additional_info = request.POST.get('additional_info', '')
            
            # Validate required fields
            if not all([name, email, phone]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('mortgage_calculator')
            
            # Convert numeric fields
            home_price_decimal = None
            down_payment_decimal = None
            loan_term_int = None
            
            if home_price:
                try:
                    home_price_decimal = float(home_price)
                except ValueError:
                    pass
            
            if down_payment:
                try:
                    down_payment_decimal = float(down_payment)
                except ValueError:
                    pass
            
            if loan_term:
                try:
                    loan_term_int = int(loan_term)
                except ValueError:
                    pass
            
            # Get system info
            from .webhook_utils import get_client_ip, get_system_info
            system_info = get_system_info(request)
            
            # Create the inquiry with safety truncation
            inquiry = MortgageInquiry.objects.create(
                name=name[:100] if name else None,  # Truncate to 100 chars
                email=email,
                phone=phone[:20] if phone else None,  # Truncate to 20 chars
                property_type=property_type[:50] if property_type else None,  # Truncate to 50 chars
                home_price=home_price_decimal,
                down_payment=down_payment_decimal,
                loan_term=loan_term_int,
                credit_score=credit_score[:50] if credit_score else None,  # Truncate to 50 chars
                additional_info=additional_info if additional_info else None,  # TextField, no truncation needed
                ip_address=system_info.get('ip_address'),
                user_agent=system_info.get('user_agent'),  # TextField, no truncation needed
                referrer=system_info.get('referrer'),
                language=system_info.get('language')[:50] if system_info.get('language') else None  # Truncate to 50 chars
            )
            
            # Send to CRM via webhook
            from .webhook_utils import send_to_crm, format_mortgage_inquiry_data
            form_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'property_type': property_type,
                'home_price': home_price,
                'down_payment': down_payment,
                'loan_term': loan_term,
                'interest_rate': request.POST.get('interest_rate', ''),
                'calculated_payment': request.POST.get('calculated_payment', ''),
                'location': request.POST.get('location', ''),
                'message': additional_info,
                'preferred_contact_time': request.POST.get('preferred_contact_time', '')
            }
            lead_data = format_mortgage_inquiry_data(form_data)
            send_to_crm('mortgage_inquiry', lead_data, request)
            
            messages.success(request, f'Thank you for your mortgage inquiry, {name}! Our team will analyze your situation and provide you with personalized mortgage information within 24 hours.')
            return redirect('mortgage_calculator')
            
        except Exception as e:
            messages.error(request, f'There was an error submitting your inquiry. Please try again. Error: {str(e)}')
            return redirect('mortgage_calculator')
    
    # If not POST, redirect to mortgage calculator page
    return redirect('mortgage_calculator')


def terms_of_service(request):
    """Terms of Service page"""
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/terms_of_service.html', context)


def privacy_policy(request):
    """Privacy Policy page"""
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/privacy_policy.html', context)


def cookie_policy(request):
    """Cookie Policy page"""
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Raj/cookie_policy.html', context)


def tracked_blog_detail_new(request, post_id, customer_code):
    """New blog tracking with clean URL format: /blog/<post_id>/<customer_code>/"""
    try:
        # Get the blog post
        post = get_object_or_404(BlogPost, id=post_id, published=True)
        
        # Create or get tracking record
        tracking, created = BlogTracking.objects.get_or_create(
            blog_post_id=post_id,
            member_name=customer_code,  # Using customer_code as member_name for now
            defaults={
                'member_email': f'{customer_code}@tracking.local',
                'member_phone': '',
                'crm_reference': customer_code,
            }
        )
        
        # Mark as opened if not already opened
        if not tracking.is_opened:
            # Get client IP and user agent
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            tracking.mark_as_opened(ip_address=ip_address, user_agent=user_agent)
            
            # Send real-time notification to Podium webhook
            webhook_data = {
                'tracking_code': str(tracking.tracking_code),
                'member_name': tracking.member_name,
                'member_phone': tracking.member_phone,
                'member_email': tracking.member_email,
                'blog_post_id': tracking.blog_post_id,
                'crm_reference': tracking.crm_reference,
                'opened_at': tracking.opened_at.isoformat() if tracking.opened_at else None,
                'ip_address': ip_address,
                'user_agent': user_agent,
                'referrer': request.META.get('HTTP_REFERER', ''),
                'language': request.META.get('HTTP_ACCEPT_LANGUAGE', ''),
            }
            
            # Send to CRM
            from .webhook_utils import send_link_tracking_to_crm
            send_link_tracking_to_crm(tracking, request)
        
        # Render the blog post normally
        context = {
            'post': post,
            'brand_name': settings.BRAND_NAME,
            'tracking_code': str(tracking.tracking_code),
            'customer_code': customer_code,
        }
        return render(request, 'Raj/blog_detail.html', context)
        
    except Exception as e:
        # If there's an error, redirect to the blog post without tracking
        return redirect('blog_detail', post_id=post_id)


def tracked_open_house(request, customer_code):
    """Tracked open house page with customer code"""
    return _tracked_page_view(request, 'open-house', 'open-house', customer_code, 'open_house')

def tracked_selling(request, customer_code):
    """Tracked selling page with customer code"""
    return _tracked_page_view(request, 'selling', 'selling', customer_code, 'selling')

def tracked_buy_lease(request, customer_code):
    """Tracked buy-lease page with customer code"""
    return _tracked_page_view(request, 'buy-lease', 'buy-lease', customer_code, 'buy_lease')

def tracked_mortgage_calculator(request, customer_code):
    """Tracked mortgage calculator page with customer code"""
    return _tracked_page_view(request, 'mortgage-calculator', 'mortgage-calculator', customer_code, 'mortgage_calculator')

def _tracked_page_view(request, page_type, page_id, customer_code, template_name):
    """Generic tracked page view that handles tracking and renders the page"""
    try:
        from .models import LinkTracking
        from .webhook_utils import get_client_ip, send_link_tracking_to_crm
        
        # Create or get tracking record
        tracking, created = LinkTracking.objects.get_or_create(
            customer_code=customer_code,
            defaults={
                'customer_name': customer_code,
                'customer_email': f'{customer_code}@tracking.local',
                'page_type': page_type,
                'page_id': page_id,
                'original_url': request.build_absolute_uri(),
                'tracked_url': request.build_absolute_uri(),
            }
        )
        
        # Record the click
        tracking.record_click(
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referrer=request.META.get('HTTP_REFERER', ''),
            language=request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        )
        
        # Send to CRM
        send_link_tracking_to_crm(tracking, request)
        
    except Exception as e:
        # If tracking fails, still render the page
        pass
    
    # Render the appropriate page with tracking context
    if template_name == 'open_house':
        return open_house(request)
    elif template_name == 'selling':
        return selling(request)
    elif template_name == 'buy_lease':
        return buy_lease(request)
    elif template_name == 'mortgage_calculator':
        return mortgage_calculator(request)
    else:
        # Fallback to home
        return redirect('home')

def general_tracking_redirect(request, customer_code):
    """General tracking redirect for customer codes like /ju131"""
    # List of protected URL patterns that should NOT be treated as tracking
    protected_patterns = [
        'admin', 'buy-lease', 'selling', 'blog', 'open-house', 
        'mortgage-calculator', 'terms-of-service', 'privacy-policy', 
        'cookie-policy', 'static', 'media', 'favicon.ico',
        'api', 'tracking-dashboard', 'blog-admin'
    ]
    
    # Check if customer_code matches a protected pattern
    if customer_code in protected_patterns:
        from django.http import Http404
        raise Http404("Page not found")
    
    # Create a general tracking record
    try:
        from .models import LinkTracking
        from .webhook_utils import get_client_ip, send_link_tracking_to_crm
        
        # Create or get tracking record
        tracking, created = LinkTracking.objects.get_or_create(
            customer_code=customer_code,
            defaults={
                'customer_name': customer_code,
                'customer_email': f'{customer_code}@tracking.local',
                'page_type': 'home',
                'page_id': 'home',
                'original_url': request.build_absolute_uri(),
                'tracked_url': request.build_absolute_uri(),
            }
        )
        
        # Record the click
        tracking.record_click(
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referrer=request.META.get('HTTP_REFERER', ''),
            language=request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        )
        
        # Send to CRM
        send_link_tracking_to_crm(tracking, request)
        
    except Exception as e:
        # If tracking fails, still redirect to home
        pass
    
    # Redirect to home page with tracking
    return redirect('home')


