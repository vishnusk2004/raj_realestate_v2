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
from .models import BlogTracking, BlogPost
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
        podium_url = "https://workflow-automation.podio.com/catch/8g78a8102321zec"
        
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

        # Pass the updated queryset as context
        context = {
            'featured_properties': featured_properties,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Henry/index.html', context)
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
    return render(request, 'Henry/featured_properties.html', context)


def blog(request):
    """Blog page view"""
    try:
        # Get published blog posts from database
        posts = BlogPost.objects.filter(published=True).order_by('-featured', '-created_at')
        
        context = {
            'posts': posts,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Henry/blog.html', context)
    except Exception as e:
        print(f"Error in blog view: {e}")
        return render(request, 'Henry/blog.html', {'posts': [], 'brand_name': settings.BRAND_NAME})


def blog_detail(request, post_id):
    """Blog detail page view"""
    try:
        # Get the specific blog post from database
        post = get_object_or_404(BlogPost, id=post_id, published=True)
        
        # Get related posts (exclude current post, limit to 2)
        related_posts = BlogPost.objects.filter(published=True).exclude(id=post_id).order_by('-featured', '-created_at')[:2]
        
        context = {
            'post': post,
            'related_posts': related_posts,
            'brand_name': settings.BRAND_NAME
        }
        return render(request, 'Henry/blog_detail.html', context)
    except Exception as e:
        print(f"Error in blog_detail view: {e}")
        return HttpResponse("Blog post not found", status=404)


def blog_page(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/blog_page.html', context)


def buying(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/buying.html', context)


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
            
            # Create and save the contact
            contact = SellingContact.objects.create(
                name=name,
                email=email,
                phone=phone,
                property_address=property_address,
                property_type=property_type,
                estimated_value=estimated_value,
                timeline=timeline,
                message=message
            )
            
            messages.success(request, 'Thank you! Our team will contact you within 24 hours.')
            return redirect('selling')
            
        except Exception as e:
            messages.error(request, 'There was an error submitting your request. Please try again.')
    
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/selling.html', context)


def leasing(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/leasing.html', context)


def home_valuation(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/home_valuation.html', context)


def open_house(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/open_house.html', context)


def mortgage_calculator(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/mortgage_calculator.html', context)


def market_insights(request):
    context = {
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/market_insights.html', context)


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
        return render(request, 'Henry/blog_detail.html', context)
        
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
            
            # Generate the tracking URL
            tracking_url = request.build_absolute_uri(f'/tracked-blog/{tracking.tracking_code}/')
            
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
    
    return render(request, 'Henry/tracking_dashboard.html', context)


# Blog Admin Views
def blog_admin(request):
    """Blog admin dashboard"""
    posts = BlogPost.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/blog_admin.html', context)


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
    return render(request, 'Henry/blog_form.html', context)


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
    return render(request, 'Henry/blog_form.html', context)


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
    return render(request, 'Henry/blog_delete.html', context)

