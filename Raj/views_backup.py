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
            'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
            'excerpt': 'Discover the latest insights into the real estate investment market and tips for maximizing returns.',
            'content': '''
            <h3>Understanding Real Estate Investment</h3>
            <p>Real estate investment has long been considered one of the most stable and profitable investment strategies. Whether you're a seasoned investor or just starting out, understanding the fundamentals is crucial for success.</p>
            
            <h4>Types of Real Estate Investments</h4>
            <ul>
                <li><strong>Residential Properties:</strong> Single-family homes, condos, and townhouses</li>
                <li><strong>Commercial Properties:</strong> Office buildings, retail spaces, and warehouses</li>
                <li><strong>Industrial Properties:</strong> Manufacturing facilities and distribution centers</li>
                <li><strong>Mixed-Use Properties:</strong> Combinations of residential and commercial spaces</li>
            </ul>
            
            <h4>Key Investment Strategies</h4>
            <p>There are several approaches to real estate investment, each with its own benefits and considerations:</p>
            
            <h5>1. Buy and Hold</h5>
            <p>This strategy involves purchasing properties and holding them for long-term appreciation and rental income. It's ideal for investors seeking steady cash flow and long-term wealth building.</p>
            
            <h5>2. Fix and Flip</h5>
            <p>This approach involves purchasing properties that need renovation, improving them, and selling for a profit. It requires more active involvement but can yield higher returns in shorter timeframes.</p>
            
            <h5>3. Real Estate Investment Trusts (REITs)</h5>
            <p>REITs allow investors to participate in real estate markets without directly owning properties. They offer liquidity and diversification benefits.</p>
            
            <h4>Market Analysis and Due Diligence</h4>
            <p>Before making any investment, thorough market research is essential. Consider factors such as:</p>
            <ul>
                <li>Local market trends and growth patterns</li>
                <li>Property values and rental rates</li>
                <li>Economic indicators and job market stability</li>
                <li>Infrastructure development and future plans</li>
            </ul>
            
            <h4>Risk Management</h4>
            <p>Like any investment, real estate carries risks. Diversification, proper insurance, and maintaining adequate cash reserves are crucial for managing these risks effectively.</p>
            
            <p>Remember, successful real estate investment requires patience, research, and a long-term perspective. Start small, learn continuously, and consider working with experienced professionals to guide your investment decisions.</p>
            '''
        },
        {
            'id': 2,
            'title': 'First-Time Homebuyer Guide: Everything You Need to Know',
            'author': 'Sarah Johnson',
            'date': date(2023, 10, 28),
            'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=300&fit=crop',
            'excerpt': 'A comprehensive guide for first-time homebuyers covering everything from pre-approval to closing.',
            'content': '''
            <h3>Your Journey to Homeownership</h3>
            <p>Buying your first home is one of life's most significant milestones. This comprehensive guide will walk you through every step of the process, from initial planning to closing day.</p>
            
            <h4>Step 1: Assess Your Financial Readiness</h4>
            <p>Before you start house hunting, it's crucial to understand your financial situation:</p>
            <ul>
                <li><strong>Credit Score:</strong> Aim for a score of 620 or higher for conventional loans</li>
                <li><strong>Down Payment:</strong> Save 20% if possible, but some programs allow as little as 3%</li>
                <li><strong>Emergency Fund:</strong> Maintain 3-6 months of expenses in savings</li>
                <li><strong>Debt-to-Income Ratio:</strong> Keep total monthly debt payments under 43% of income</li>
            </ul>
            
            <h4>Step 2: Get Pre-Approved for a Mortgage</h4>
            <p>Pre-approval gives you a clear picture of your budget and shows sellers you're a serious buyer. Gather these documents:</p>
            <ul>
                <li>Recent pay stubs and tax returns</li>
                <li>Bank statements and investment account statements</li>
                <li>Employment verification letter</li>
                <li>List of current debts and monthly payments</li>
            </ul>
            
            <h4>Step 3: Find the Right Real Estate Agent</h4>
            <p>A good agent will be your advocate throughout the process. Look for someone who:</p>
            <ul>
                <li>Has experience in your target area</li>
                <li>Understands your needs and budget</li>
                <li>Communicates clearly and promptly</li>
                <li>Has positive reviews from past clients</li>
            </ul>
            
            <h4>Step 4: House Hunting</h4>
            <p>Create a list of must-haves and nice-to-haves. Consider factors like:</p>
            <ul>
                <li>Location and neighborhood amenities</li>
                <li>School district quality</li>
                <li>Commute times to work</li>
                <li>Future resale potential</li>
                <li>Property condition and maintenance needs</li>
            </ul>
            
            <h4>Step 5: Making an Offer</h4>
            <p>Your agent will help you craft a competitive offer based on:</p>
            <ul>
                <li>Recent comparable sales in the area</li>
                <li>Market conditions and competition</li>
                <li>Property condition and inspection results</li>
                <li>Your budget and timeline</li>
            </ul>
            
            <h4>Step 6: Home Inspection and Appraisal</h4>
            <p>These steps protect your investment:</p>
            <ul>
                <li><strong>Home Inspection:</strong> Identifies potential issues and maintenance needs</li>
                <li><strong>Appraisal:</strong> Ensures the property value matches the purchase price</li>
            </ul>
            
            <h4>Step 7: Closing Process</h4>
            <p>During the final weeks before closing:</p>
            <ul>
                <li>Review all loan documents carefully</li>
                <li>Conduct a final walkthrough of the property</li>
                <li>Prepare for closing costs (typically 2-5% of purchase price)</li>
                <li>Bring required identification and certified funds</li>
            </ul>
            
            <h4>Common First-Time Buyer Mistakes to Avoid</h4>
            <ul>
                <li>Not getting pre-approved before house hunting</li>
                <li>Making major purchases before closing</li>
                <li>Skipping the home inspection</li>
                <li>Not budgeting for closing costs and moving expenses</li>
                <li>Falling in love with the first house you see</li>
            </ul>
            
            <p>Remember, buying a home is a process that requires patience and preparation. Take your time, ask questions, and don't hesitate to seek professional guidance when needed.</p>
            '''
        },
        {
            'id': 3,
            'title': 'Market Trends: What to Expect in 2024',
            'author': 'Michael Chen',
            'date': date(2023, 10, 25),
            'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
            'excerpt': 'An analysis of current real estate market trends and predictions for the coming year.',
            'content': '''
            <h3>Real Estate Market Outlook for 2024</h3>
            <p>As we look ahead to 2024, several key trends are shaping the real estate landscape. Understanding these patterns can help both buyers and sellers make informed decisions.</p>
            
            <h4>Interest Rate Environment</h4>
            <p>The Federal Reserve's monetary policy continues to influence mortgage rates. While rates have stabilized somewhat, they remain higher than the historic lows of recent years. This has created a "lock-in effect" where many homeowners are reluctant to sell their current properties.</p>
            
            <h4>Inventory Challenges</h4>
            <p>Low inventory remains a significant factor in many markets:</p>
            <ul>
                <li>New construction has been limited due to supply chain issues and labor shortages</li>
                <li>Existing homeowners are staying put longer</li>
                <li>Investor activity has cooled in some markets</li>
            </ul>
            
            <h4>Regional Variations</h4>
            <p>Market conditions vary significantly by location:</p>
            <ul>
                <li><strong>Urban Markets:</strong> Recovery continues as remote work policies evolve</li>
                <li><strong>Suburban Areas:</strong> Still experiencing strong demand for single-family homes</li>
                <li><strong>Rural Communities:</strong> Seeing increased interest from remote workers</li>
            </ul>
            
            <h4>Technology Integration</h4>
            <p>Real estate technology continues to evolve:</p>
            <ul>
                <li>Virtual tours and 3D walkthroughs are becoming standard</li>
                <li>AI-powered pricing tools are improving accuracy</li>
                <li>Digital transaction management is streamlining processes</li>
            </ul>
            
            <h4>Affordability Concerns</h4>
            <p>Housing affordability remains a challenge in many markets. Key factors include:</p>
            <ul>
                <li>Rising home prices outpacing wage growth</li>
                <li>Higher mortgage rates increasing monthly payments</li>
                <li>Limited affordable housing inventory</li>
            </ul>
            
            <h4>Investment Opportunities</h4>
            <p>Despite challenges, opportunities exist for savvy investors:</p>
            <ul>
                <li>Distressed properties in transitioning neighborhoods</li>
                <li>Multi-family properties with strong rental demand</li>
                <li>Commercial real estate in growing business districts</li>
            </ul>
            
            <h4>What This Means for Buyers</h4>
            <ul>
                <li>Be prepared for competitive markets in desirable areas</li>
                <li>Consider expanding your search criteria</li>
                <li>Get pre-approved to strengthen your offers</li>
                <li>Work with experienced local agents</li>
            </ul>
            
            <h4>What This Means for Sellers</h4>
            <ul>
                <li>Price competitively based on current market conditions</li>
                <li>Invest in staging and minor improvements</li>
                <li>Be flexible with showing schedules</li>
                <li>Consider timing your sale strategically</li>
            </ul>
            
            <p>While market conditions can be challenging, working with experienced professionals and staying informed about local trends can help you navigate the 2024 real estate market successfully.</p>
            '''
        },
        {
            'id': 4,
            'title': 'Home Staging Tips That Sell Properties Faster',
            'author': 'Emily Rodriguez',
            'date': date(2023, 10, 22),
            'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&h=300&fit=crop',
            'excerpt': 'Professional staging techniques that help properties sell faster and for better prices.',
            'content': '''
            <h3>The Art of Home Staging</h3>
            <p>Home staging is more than just decorating—it's about creating an emotional connection that helps potential buyers envision themselves living in your space. Here are proven techniques that can help your property sell faster and for a better price.</p>
            
            <h4>First Impressions Matter</h4>
            <p>The exterior of your home creates the first impression. Focus on:</p>
            <ul>
                <li><strong>Curb Appeal:</strong> Fresh paint, clean windows, and well-maintained landscaping</li>
                <li><strong>Entryway:</strong> Clean, welcoming front door and porch area</li>
                <li><strong>Lighting:</strong> Ensure all exterior lights are working and clean</li>
            </ul>
            
            <h4>Declutter and Depersonalize</h4>
            <p>Create a neutral canvas that appeals to the widest range of buyers:</p>
            <ul>
                <li>Remove personal photos and memorabilia</li>
                <li>Clear countertops and surfaces of unnecessary items</li>
                <li>Organize closets and storage spaces</li>
                <li>Consider renting a storage unit for excess furniture</li>
            </ul>
            
            <h4>Maximize Space and Light</h4>
            <p>Make rooms feel larger and brighter:</p>
            <ul>
                <li>Remove or rearrange furniture to improve flow</li>
                <li>Use mirrors to reflect light and create the illusion of space</li>
                <li>Open curtains and blinds to let in natural light</li>
                <li>Clean all windows inside and out</li>
            </ul>
            
            <h4>Neutral Color Palette</h4>
            <p>Stick to neutral colors that appeal to most buyers:</p>
            <ul>
                <li>Paint walls in light, neutral tones</li>
                <li>Use white or light-colored bedding and towels</li>
                <li>Avoid bold or trendy color schemes</li>
                <li>Add pops of color through accessories and artwork</li>
            </ul>
            
            <h4>Room-by-Room Staging Tips</h4>
            
            <h5>Living Room</h5>
            <ul>
                <li>Arrange furniture to create conversation areas</li>
                <li>Add fresh flowers or plants</li>
                <li>Ensure comfortable seating for potential buyers</li>
                <li>Remove any signs of pets or smoking</li>
            </ul>
            
            <h5>Kitchen</h5>
            <ul>
                <li>Clear countertops of all appliances and clutter</li>
                <li>Add a bowl of fresh fruit or flowers</li>
                <li>Ensure all appliances are clean and working</li>
                <li>Consider updating cabinet hardware if outdated</li>
            </ul>
            
            <h5>Bedrooms</h5>
            <ul>
                <li>Make beds with fresh, neutral linens</li>
                <li>Remove personal items from nightstands</li>
                <li>Ensure adequate lighting for reading</li>
                <li>Keep closets organized and not overcrowded</li>
            </ul>
            
            <h5>Bathrooms</h5>
            <ul>
                <li>Deep clean all surfaces and fixtures</li>
                <li>Add fresh towels and bath accessories</li>
                <li>Remove personal toiletries</li>
                <li>Ensure good ventilation and lighting</li>
            </ul>
            
            <h4>Professional Staging vs. DIY</h4>
            <p>Consider your options:</p>
            <ul>
                <li><strong>Professional Staging:</strong> Higher cost but often yields better results</li>
                <li><strong>DIY Staging:</strong> More cost-effective but requires time and effort</li>
                <li><strong>Virtual Staging:</strong> Cost-effective option for vacant properties</li>
            </ul>
            
            <h4>Seasonal Considerations</h4>
            <p>Adapt your staging to the season:</p>
            <ul>
                <li><strong>Spring/Summer:</strong> Emphasize outdoor living spaces</li>
                <li><strong>Fall/Winter:</strong> Create cozy, warm atmospheres</li>
                <li>Use seasonal decorations sparingly and tastefully</li>
            </ul>
            
            <h4>Common Staging Mistakes to Avoid</h4>
            <ul>
                <li>Over-staging with too many accessories</li>
                <li>Ignoring maintenance issues</li>
                <li>Using outdated or worn furniture</li>
                <li>Neglecting outdoor spaces</li>
                <li>Forgetting about lighting and temperature</li>
            </ul>
            
            <p>Remember, the goal of staging is to help buyers imagine themselves living in your home. Keep it simple, clean, and appealing to the broadest audience possible.</p>
            '''
        },
        {
            'id': 5,
            'title': 'Understanding Mortgage Options in Today\'s Market',
            'author': 'David Thompson',
            'date': date(2023, 10, 20),
            'image_url': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400&h=300&fit=crop',
            'excerpt': 'A comprehensive overview of different mortgage types and how to choose the right one for your situation.',
            'content': '''
            <h3>Navigating Mortgage Options</h3>
            <p>Choosing the right mortgage is one of the most important financial decisions you'll make. With various loan types available, understanding your options can save you thousands of dollars over the life of your loan.</p>
            
            <h4>Conventional Loans</h4>
            <p>These are the most common type of mortgage:</p>
            <ul>
                <li><strong>Fixed-Rate Mortgages:</strong> Interest rate remains constant throughout the loan term</li>
                <li><strong>Adjustable-Rate Mortgages (ARMs):</strong> Interest rate can change after an initial fixed period</li>
                <li>Typically require 20% down payment to avoid private mortgage insurance (PMI)</li>
                <li>Good credit score (620+) usually required</li>
            </ul>
            
            <h4>Government-Backed Loans</h4>
            
            <h5>FHA Loans</h5>
            <ul>
                <li>Insured by the Federal Housing Administration</li>
                <li>Lower down payment requirements (as low as 3.5%)</li>
                <li>More flexible credit requirements</li>
                <li>Mortgage insurance required for the life of the loan</li>
            </ul>
            
            <h5>VA Loans</h5>
            <ul>
                <li>Available to eligible veterans and active military</li>
                <li>No down payment required</li>
                <li>No private mortgage insurance</li>
                <li>Competitive interest rates</li>
            </ul>
            
            <h5>USDA Loans</h5>
            <ul>
                <li>For rural and suburban areas</li>
                <li>No down payment required</li>
                <li>Income limits apply</li>
                <li>Property must be in eligible rural areas</li>
            </ul>
            
            <h4>Jumbo Loans</h4>
            <p>For high-value properties that exceed conventional loan limits:</p>
            <ul>
                <li>Higher down payment requirements (typically 20%+)</li>
                <li>Stricter credit requirements</li>
                <li>Higher interest rates</li>
                <li>Used for luxury properties in expensive markets</li>
            </ul>
            
            <h4>Fixed vs. Adjustable Rate</h4>
            
            <h5>Fixed-Rate Mortgages</h5>
            <p>Best for buyers who:</p>
            <ul>
                <li>Plan to stay in the home long-term</li>
                <li>Want predictable monthly payments</li>
                <li>Prefer stability over potential savings</li>
            </ul>
            
            <h5>Adjustable-Rate Mortgages (ARMs)</h5>
            <p>Best for buyers who:</p>
            <ul>
                <li>Plan to move or refinance within 5-7 years</li>
                <li>Expect income to increase significantly</li>
                <li>Are comfortable with payment uncertainty</li>
            </ul>
            
            <h4>Loan Terms</h4>
            <p>Common mortgage terms and their benefits:</p>
            <ul>
                <li><strong>15-Year:</strong> Higher monthly payments but less total interest</li>
                <li><strong>30-Year:</strong> Lower monthly payments but more total interest</li>
                <li><strong>20-Year:</strong> Balance between payment amount and interest savings</li>
            </ul>
            
            <h4>Pre-Approval Process</h4>
            <p>Getting pre-approved involves:</p>
            <ul>
                <li>Credit check and income verification</li>
                <li>Asset documentation</li>
                <li>Debt-to-income ratio calculation</li>
                <li>Loan amount determination</li>
            </ul>
            
            <h4>Closing Costs</h4>
            <p>Be prepared for additional costs:</p>
            <ul>
                <li>Origination fees and points</li>
                <li>Title insurance and escrow fees</li>
                <li>Appraisal and inspection costs</li>
                <li>Recording fees and taxes</li>
            </ul>
            
            <h4>Tips for Getting the Best Rate</h4>
            <ul>
                <li>Shop around with multiple lenders</li>
                <li>Improve your credit score before applying</li>
                <li>Consider paying points to lower your rate</li>
                <li>Maintain stable employment and income</li>
                <li>Keep debt-to-income ratio low</li>
            </ul>
            
            <h4>Refinancing Considerations</h4>
            <p>Consider refinancing when:</p>
            <ul>
                <li>Interest rates drop significantly</li>
                <li>Your credit score improves</li>
                <li>You want to change loan terms</li>
                <li>You need to access home equity</li>
            </ul>
            
            <p>Remember, the best mortgage for you depends on your financial situation, goals, and timeline. Work with a qualified mortgage professional to explore all your options and find the loan that best fits your needs.</p>
            '''
        },
        {
            'id': 6,
            'title': 'Luxury Real Estate: What High-End Buyers Want',
            'author': 'Jennifer Martinez',
            'date': date(2023, 10, 18),
            'image_url': 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=400&h=300&fit=crop',
            'excerpt': 'Insights into the luxury real estate market and what high-end buyers are looking for.',
            'content': '''
            <h3>The Luxury Real Estate Market</h3>
            <p>The luxury real estate market operates by different rules than the traditional housing market. Understanding what high-end buyers value can help both buyers and sellers navigate this exclusive segment successfully.</p>
            
            <h4>Location, Location, Location</h4>
            <p>For luxury buyers, location is paramount:</p>
            <ul>
                <li><strong>Prime Neighborhoods:</strong> Established, prestigious areas with strong property values</li>
                <li><strong>Waterfront Properties:</strong> Oceanfront, lakefront, or riverfront locations</li>
                <li><strong>Mountain Views:</strong> Properties with stunning natural vistas</li>
                <li><strong>Urban Penthouses:</strong> High-rise living in city centers</li>
            </ul>
            
            <h4>Privacy and Security</h4>
            <p>Luxury buyers prioritize privacy and security:</p>
            <ul>
                <li>Gated communities with 24/7 security</li>
                <li>Private driveways and secluded entrances</li>
                <li>Advanced security systems and surveillance</li>
                <li>Private beaches, docks, or recreational facilities</li>
            </ul>
            
            <h4>Architectural Excellence</h4>
            <p>High-end buyers appreciate exceptional design:</p>
            <ul>
                <li>Custom architecture and unique design elements</li>
                <li>High-quality materials and finishes</li>
                <li>Attention to detail in every aspect</li>
                <li>Integration with natural surroundings</li>
            </ul>
            
            <h4>Premium Amenities</h4>
            <p>Luxury properties often include resort-style amenities:</p>
            <ul>
                <li><strong>Outdoor Living:</strong> Infinity pools, outdoor kitchens, and entertainment areas</li>
                <li><strong>Wellness Features:</strong> Home gyms, spas, and meditation rooms</li>
                <li><strong>Entertainment:</strong> Home theaters, wine cellars, and game rooms</li>
                <li><strong>Smart Home Technology:</strong> Integrated automation and security systems</li>
            </ul>
            
            <h4>Space and Scale</h4>
            <p>Luxury buyers expect generous proportions:</p>
            <ul>
                <li>High ceilings and open floor plans</li>
                <li>Multiple living areas and entertaining spaces</li>
                <li>Guest suites and staff quarters</li>
                <li>Extensive storage and utility areas</li>
            </ul>
            
            <h4>Kitchen and Dining</h4>
            <p>The kitchen is often the heart of luxury homes:</p>
            <ul>
                <li>Professional-grade appliances and equipment</li>
                <li>Custom cabinetry and premium countertops</li>
                <li>Large islands and breakfast areas</li>
                <li>Walk-in pantries and wine storage</li>
            </ul>
            
            <h4>Master Suite Features</h4>
            <p>Luxury master suites are designed for comfort and relaxation:</p>
            <ul>
                <li>Spacious bedrooms with sitting areas</li>
                <li>Luxurious master bathrooms with premium fixtures</li>
                <li>Walk-in closets with custom organization</li>
                <li>Private balconies or terraces</li>
            </ul>
            
            <h4>Outdoor Living Spaces</h4>
            <p>Luxury buyers value exceptional outdoor areas:</p>
            <ul>
                <li>Landscaped gardens and outdoor entertainment areas</li>
                <li>Infinity pools with spa features</li>
                <li>Outdoor kitchens and dining areas</li>
                <li>Fire features and outdoor lighting</li>
            </ul>
            
            <h4>Technology Integration</h4>
            <p>Smart home features are expected in luxury properties:</p>
            <ul>
                <li>Integrated home automation systems</li>
                <li>Advanced security and surveillance</li>
                <li>Climate control and energy management</li>
                <li>Entertainment and audio-visual systems</li>
            </ul>
            
            <h4>Investment Considerations</h4>
            <p>Luxury real estate can be a sound investment:</p>
            <ul>
                <li>Limited supply in prime locations</li>
                <li>Potential for appreciation in desirable markets</li>
                <li>Rental income opportunities</li>
                <li>Portfolio diversification benefits</li>
            </ul>
            
            <h4>Working with Luxury Buyers</h4>
            <p>Luxury transactions require specialized expertise:</p>
            <ul>
                <li>Discretion and confidentiality</li>
                <li>Understanding of unique financing options</li>
                <li>Access to off-market properties</li>
                <li>Experience with complex transaction structures</li>
            </ul>
            
            <h4>Market Trends</h4>
            <p>Current trends in luxury real estate include:</p>
            <ul>
                <li>Increased demand for wellness-focused amenities</li>
                <li>Growing interest in sustainable and eco-friendly features</li>
                <li>Integration of work-from-home spaces</li>
                <li>Focus on outdoor living and connection to nature</li>
            </ul>
            
            <p>The luxury real estate market continues to evolve, with buyers seeking properties that offer not just exceptional living spaces, but also unique experiences and lifestyle benefits. Understanding these preferences is key to success in this exclusive market segment.</p>
            '''
        }
    ]
    
    # Find the specific post
    post = None
    for p in posts:
        if p['id'] == post_id:
            post = p
            break
    
    if not post:
        return HttpResponse("Blog post not found", status=404)
    
    # Get related posts (exclude current post)
    related_posts = [p for p in posts if p['id'] != post_id][:2]
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'brand_name': settings.BRAND_NAME
    }
    return render(request, 'Henry/blog_detail.html', context)


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
        
        # Get the blog post data (same as in blog_detail view)
        posts = [
            {
                'id': 1,
                'title': 'Exploring Real Estate Investment Opportunities',
                'author': 'John Doe',
                'date': date(2023, 11, 1),
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'excerpt': 'Discover the latest insights into the real estate investment market and tips for maximizing returns.',
                'content': '''
                <h3>Understanding Real Estate Investment</h3>
                <p>Real estate investment has long been considered one of the most stable and profitable investment strategies. Whether you're a seasoned investor or just starting out, understanding the fundamentals is crucial for success.</p>
                
                <h4>Types of Real Estate Investments</h4>
                <ul>
                    <li><strong>Residential Properties:</strong> Single-family homes, condos, and townhouses</li>
                    <li><strong>Commercial Properties:</strong> Office buildings, retail spaces, and warehouses</li>
                    <li><strong>Industrial Properties:</strong> Manufacturing facilities and distribution centers</li>
                    <li><strong>Mixed-Use Properties:</strong> Combinations of residential and commercial spaces</li>
                </ul>
                
                <h4>Benefits of Real Estate Investment</h4>
                <p>Real estate offers several advantages over other investment types:</p>
                <ul>
                    <li><strong>Appreciation:</strong> Property values tend to increase over time</li>
                    <li><strong>Cash Flow:</strong> Rental income provides regular monthly returns</li>
                    <li><strong>Tax Benefits:</strong> Deductions for mortgage interest, depreciation, and expenses</li>
                    <li><strong>Leverage:</strong> Ability to control large assets with relatively small down payments</li>
                    <li><strong>Inflation Hedge:</strong> Real estate typically keeps pace with inflation</li>
                </ul>
                
                <h4>Getting Started</h4>
                <p>Before diving into real estate investment, consider these steps:</p>
                <ol>
                    <li><strong>Set Clear Goals:</strong> Define your investment objectives and timeline</li>
                    <li><strong>Research Markets:</strong> Study local market conditions and trends</li>
                    <li><strong>Build Your Team:</strong> Find reliable real estate agents, contractors, and property managers</li>
                    <li><strong>Secure Financing:</strong> Explore loan options and get pre-approved</li>
                    <li><strong>Start Small:</strong> Consider beginning with a single-family rental property</li>
                </ol>
                
                <h4>Risk Management</h4>
                <p>Like any investment, real estate comes with risks:</p>
                <ul>
                    <li>Market fluctuations and economic downturns</li>
                    <li>Property maintenance and repair costs</li>
                    <li>Vacancy periods and tenant issues</li>
                    <li>Interest rate changes affecting financing costs</li>
                </ul>
                
                <p>Diversification across different property types and locations can help mitigate these risks.</p>
                '''
            },
            {
                'id': 2,
                'title': 'First-Time Homebuyer Guide: Everything You Need to Know',
                'author': 'Sarah Johnson',
                'date': date(2023, 10, 28),
                'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=300&fit=crop',
                'excerpt': 'A comprehensive guide for first-time homebuyers covering everything from pre-approval to closing.',
                'content': '''
                <h3>Your Journey to Homeownership</h3>
                <p>Buying your first home is one of life's most significant milestones. This comprehensive guide will walk you through every step of the process, from initial planning to closing day.</p>
                
                <h4>Step 1: Assess Your Financial Situation</h4>
                <p>Before you start house hunting, it's crucial to understand your financial position:</p>
                <ul>
                    <li>Calculate your debt-to-income ratio</li>
                    <li>Review your credit score and credit report</li>
                    <li>Determine how much you can afford for a down payment</li>
                    <li>Consider additional costs like closing fees, moving expenses, and immediate repairs</li>
                </ul>
                
                <h4>Step 2: Get Pre-Approved for a Mortgage</h4>
                <p>Pre-approval gives you several advantages:</p>
                <ul>
                    <li>Shows sellers you're a serious buyer</li>
                    <li>Helps you understand your budget limits</li>
                    <li>Speeds up the closing process once you find a home</li>
                </ul>
                
                <p>Gather these documents for pre-approval:</p>
                <ul>
                    <li>Bank statements and investment account statements</li>
                    <li>Employment verification letter</li>
                    <li>List of current debts and monthly payments</li>
                </ul>
                
                <h4>Step 3: Find the Right Real Estate Agent</h4>
                <p>A good agent will be your advocate throughout the process. Look for someone who:</p>
                <ul>
                    <li>Has experience in your target area</li>
                    <li>Understands your needs and budget</li>
                    <li>Communicates clearly and promptly</li>
                    <li>Has positive reviews from past clients</li>
                </ul>
                
                <h4>Step 4: House Hunting</h4>
                <p>Create a list of must-haves and nice-to-haves. Consider factors like:</p>
                <ul>
                    <li>Location and neighborhood amenities</li>
                    <li>School district quality</li>
                    <li>Commute times to work</li>
                    <li>Future resale potential</li>
                    <li>Property condition and maintenance needs</li>
                </ul>
                
                <h4>Step 5: Making an Offer</h4>
                <p>Your agent will help you craft a competitive offer based on:</p>
                <ul>
                    <li>Recent comparable sales in the area</li>
                    <li>Market conditions and competition</li>
                    <li>Property condition and inspection results</li>
                    <li>Your budget and timeline</li>
                </ul>
                
                <h4>Step 6: Home Inspection and Appraisal</h4>
                <p>These steps protect your investment:</p>
                <ul>
                    <li><strong>Home Inspection:</strong> Identifies potential issues and maintenance needs</li>
                    <li><strong>Appraisal:</strong> Ensures the property value matches the purchase price</li>
                </ul>
                
                <h4>Step 7: Closing Process</h4>
                <p>During the final weeks before closing:</p>
                <ul>
                    <li>Review all loan documents carefully</li>
                    <li>Conduct a final walkthrough of the property</li>
                    <li>Prepare for closing costs (typically 2-5% of purchase price)</li>
                    <li>Bring required identification and certified funds</li>
                </ul>
                
                <h4>Common First-Time Buyer Mistakes to Avoid</h4>
                <ul>
                    <li>Not getting pre-approved before house hunting</li>
                    <li>Focusing only on the purchase price (ignoring other costs)</li>
                    <li>Making emotional decisions without considering resale value</li>
                    <li>Skipping the home inspection to save money</li>
                    <li>Not shopping around for the best mortgage rates</li>
                </ul>
                
                <p>Remember, buying a home is a significant financial commitment. Take your time, ask questions, and don't hesitate to seek professional advice throughout the process.</p>
                '''
            },
            {
                'id': 3,
                'title': 'Market Trends: What to Expect in 2024',
                'author': 'Michael Chen',
                'date': date(2023, 10, 25),
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'excerpt': 'An analysis of current real estate market trends and predictions for the coming year.',
                'content': '''
                <h3>Real Estate Market Outlook for 2024</h3>
                <p>As we look ahead to 2024, several key trends are shaping the real estate landscape. Understanding these patterns can help both buyers and sellers make informed decisions.</p>
                
                <h4>Interest Rate Environment</h4>
                <p>The Federal Reserve's monetary policy continues to influence mortgage rates. While rates have stabilized somewhat, they remain higher than the historic lows of recent years. This has created a "lock-in effect" where homeowners are reluctant to sell and give up their low-rate mortgages.</p>
                
                <h4>Inventory Challenges</h4>
                <p>Housing inventory remains constrained in most markets due to:</p>
                <ul>
                    <li>Limited new construction in recent years</li>
                    <li>Homeowners staying put due to low mortgage rates</li>
                    <li>High construction costs affecting new development</li>
                </ul>
                
                <h4>Price Appreciation Patterns</h4>
                <p>While price growth has moderated from the rapid increases of 2020-2022, most markets continue to see modest appreciation. However, the rate of growth varies significantly by location and property type.</p>
                
                <h4>Technology Integration</h4>
                <p>Real estate technology continues to evolve, with virtual tours, AI-powered property valuations, and digital transaction management becoming standard tools in the industry.</p>
                
                <h4>Demographic Shifts</h4>
                <p>Millennials are now the largest group of homebuyers, driving demand for starter homes and properties in walkable neighborhoods. Meanwhile, Baby Boomers are increasingly looking to downsize or relocate to retirement-friendly areas.</p>
                
                <h4>Regional Variations</h4>
                <p>Market conditions vary significantly by region. While some areas experience continued growth, others may see price corrections or slower appreciation rates.</p>
                
                <h4>Investment Opportunities</h4>
                <p>For investors, 2024 presents both challenges and opportunities. Higher interest rates affect financing costs, but rental demand remains strong in many markets, supporting cash flow potential.</p>
                
                <h4>What This Means for You</h4>
                <p>Whether you're buying, selling, or investing, staying informed about market trends is crucial. Consider working with local real estate professionals who understand your specific market conditions and can provide personalized guidance based on current trends.</p>
                '''
            },
            {
                'id': 4,
                'title': 'Home Staging Tips That Sell Properties Faster',
                'author': 'Emily Rodriguez',
                'date': date(2023, 10, 22),
                'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&h=300&fit=crop',
                'excerpt': 'Professional staging techniques that help properties sell faster and for better prices.',
                'content': '''
                <h3>The Art of Home Staging</h3>
                <p>Home staging is more than just decorating—it's about creating an emotional connection that helps potential buyers envision themselves living in your space. Here are proven techniques that can help your property sell faster and for a better price.</p>
                
                <h4>Declutter and Depersonalize</h4>
                <p>The first step in staging is removing personal items and excess clutter:</p>
                <ul>
                    <li>Pack away family photos and personal memorabilia</li>
                    <li>Remove excess furniture to make rooms feel larger</li>
                    <li>Clear countertops and surfaces of unnecessary items</li>
                    <li>Organize closets and storage spaces</li>
                </ul>
                
                <h4>Maximize Curb Appeal</h4>
                <p>First impressions matter. Enhance your home's exterior:</p>
                <ul>
                    <li>Keep the lawn mowed and landscaping trimmed</li>
                    <li>Add fresh mulch and seasonal plants</li>
                    <li>Clean or repaint the front door</li>
                    <li>Ensure outdoor lighting is working properly</li>
                </ul>
                
                <h4>Create a Neutral Palette</h4>
                <p>Neutral colors appeal to the widest range of buyers:</p>
                <ul>
                    <li>Paint walls in light, neutral tones</li>
                    <li>Use neutral furniture and accessories</li>
                    <li>Avoid bold or trendy color schemes</li>
                    <li>Add pops of color through easily changeable items like pillows or artwork</li>
                </ul>
                
                <h4>Optimize Room Function</h4>
                <p>Make sure each room has a clear, obvious purpose:</p>
                <ul>
                    <li>Convert unused spaces into functional areas</li>
                    <li>Arrange furniture to highlight room flow</li>
                    <li>Create conversation areas in living spaces</li>
                    <li>Set up a home office if space allows</li>
                </ul>
                
                <h4>Enhance Lighting</h4>
                <p>Good lighting makes spaces feel welcoming and spacious:</p>
                <ul>
                    <li>Open all curtains and blinds during showings</li>
                    <li>Turn on all lights, even during daytime</li>
                    <li>Add lamps to dark corners</li>
                    <li>Replace any burned-out bulbs</li>
                </ul>
                
                <h4>Focus on Key Rooms</h4>
                <p>Prioritize staging efforts on rooms that matter most to buyers:</p>
                <ul>
                    <li><strong>Kitchen:</strong> Clean thoroughly, clear counters, add fresh flowers</li>
                    <li><strong>Master Bedroom:</strong> Make it feel like a luxury retreat</li>
                    <li><strong>Living Room:</strong> Create an inviting gathering space</li>
                    <li><strong>Bathrooms:</strong> Ensure they're spotless with fresh towels</li>
                </ul>
                
                <h4>Add Finishing Touches</h4>
                <p>Small details can make a big difference:</p>
                <ul>
                    <li>Place fresh flowers or plants in key areas</li>
                    <li>Set the dining table for an elegant meal</li>
                    <li>Add cozy throws and decorative pillows</li>
                    <li>Ensure all rooms smell fresh and clean</li>
                </ul>
                
                <h4>Professional vs. DIY Staging</h4>
                <p>While professional staging can be expensive, it often pays for itself through faster sales and higher offers. If you're staging yourself, focus on the basics and consider hiring a professional for the most important rooms.</p>
                
                <p>Remember, the goal of staging is to help buyers imagine themselves living in your home. Keep it simple, clean, and appealing to the broadest possible audience.</p>
                '''
            },
            {
                'id': 5,
                'title': 'Understanding Mortgage Options in Today\'s Market',
                'author': 'David Thompson',
                'date': date(2023, 10, 20),
                'image_url': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400&h=300&fit=crop',
                'excerpt': 'A comprehensive overview of different mortgage types and how to choose the right one for your situation.',
                'content': '''
                <h3>Navigating Mortgage Options</h3>
                <p>Choosing the right mortgage is one of the most important financial decisions you'll make. With various loan types available, understanding your options can save you thousands of dollars over the life of your loan.</p>
                
                <h4>Conventional Loans</h4>
                <p>Conventional loans are the most common type of mortgage:</p>
                <ul>
                    <li>Not backed by government agencies</li>
                    <li>Typically require 5-20% down payment</li>
                    <li>Good credit score requirements (usually 620+)</li>
                    <li>Private mortgage insurance (PMI) required if down payment is less than 20%</li>
                </ul>
                
                <h4>FHA Loans</h4>
                <p>Federal Housing Administration loans are popular with first-time buyers:</p>
                <ul>
                    <li>Lower down payment requirements (as low as 3.5%)</li>
                    <li>More flexible credit score requirements</li>
                    <li>Government-backed, reducing lender risk</li>
                    <li>Mortgage insurance required for the life of the loan</li>
                </ul>
                
                <h4>VA Loans</h4>
                <p>Available to veterans, active-duty service members, and eligible spouses:</p>
                <ul>
                    <li>No down payment required</li>
                    <li>No private mortgage insurance</li>
                    <li>Competitive interest rates</li>
                    <li>Funding fee may apply</li>
                </ul>
                
                <h4>USDA Loans</h4>
                <p>United States Department of Agriculture loans for rural areas:</p>
                <ul>
                    <li>No down payment required</li>
                    <li>Income limits apply</li>
                    <li>Property must be in eligible rural area</li>
                    <li>Guarantee fee required</li>
                </ul>
                
                <h4>Fixed vs. Adjustable Rate Mortgages</h4>
                <p><strong>Fixed-Rate Mortgages:</strong></p>
                <ul>
                    <li>Interest rate stays the same for the entire loan term</li>
                    <li>Predictable monthly payments</li>
                    <li>Good for long-term homeowners</li>
                    <li>Higher initial rates than ARMs</li>
                </ul>
                
                <p><strong>Adjustable-Rate Mortgages (ARMs):</strong></p>
                <ul>
                    <li>Interest rate changes periodically</li>
                    <li>Lower initial rates</li>
                    <li>Good for short-term homeowners</li>
                    <li>Payment can increase over time</li>
                </ul>
                
                <h4>Jumbo Loans</h4>
                <p>For properties exceeding conforming loan limits:</p>
                <ul>
                    <li>Higher down payment requirements (often 20%+)</li>
                    <li>Stricter credit requirements</li>
                    <li>Higher interest rates</li>
                    <li>Used for luxury properties</li>
                </ul>
                
                <h4>Choosing the Right Mortgage</h4>
                <p>Consider these factors when selecting a mortgage:</p>
                <ul>
                    <li><strong>Your financial situation:</strong> Income, credit score, and available down payment</li>
                    <li><strong>How long you plan to stay:</strong> Affects whether fixed or adjustable rate makes sense</li>
                    <li><strong>Property type and location:</strong> Some loans have restrictions</li>
                    <li><strong>Future plans:</strong> Career changes, family growth, etc.</li>
                </ul>
                
                <h4>Getting Pre-Approved</h4>
                <p>Before house hunting, get pre-approved for a mortgage:</p>
                <ul>
                    <li>Shows sellers you're a serious buyer</li>
                    <li>Helps you understand your budget</li>
                    <li>Speeds up the closing process</li>
                    <li>Allows you to shop for the best rates</li>
                </ul>
                
                <p>Work with multiple lenders to compare rates and terms. Even small differences in interest rates can result in significant savings over the life of your loan.</p>
                '''
            },
            {
                'id': 6,
                'title': 'Luxury Real Estate: What High-End Buyers Want',
                'author': 'Jennifer Martinez',
                'date': date(2023, 10, 18),
                'image_url': 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=400&h=300&fit=crop',
                'excerpt': 'Insights into the luxury real estate market and what high-end buyers are looking for.',
                'content': '''
                <h3>The Luxury Real Estate Market</h3>
                <p>The luxury real estate market operates by different rules than the traditional housing market. Understanding what high-end buyers value can help both buyers and sellers navigate this exclusive segment successfully.</p>
                
                <h4>Location, Location, Location</h4>
                <p>For luxury buyers, location is paramount:</p>
                <ul>
                    <li>Prime neighborhoods with established reputations</li>
                    <li>Waterfront properties with private access</li>
                    <li>Mountain or hilltop locations with views</li>
                    <li>Proximity to cultural amenities and fine dining</li>
                    <li>Privacy and exclusivity</li>
                </ul>
                
                <h4>Architectural Excellence</h4>
                <p>Luxury buyers appreciate distinctive architecture:</p>
                <ul>
                    <li>Custom-designed homes by renowned architects</li>
                    <li>Unique architectural features and details</li>
                    <li>High-quality materials and craftsmanship</li>
                    <li>Timeless design that won't look dated</li>
                    <li>Integration with natural surroundings</li>
                </ul>
                
                <h4>Premium Amenities</h4>
                <p>Luxury properties must offer exceptional amenities:</p>
                <ul>
                    <li>Resort-style pools and outdoor living spaces</li>
                    <li>Home theaters and entertainment rooms</li>
                    <li>Wine cellars and tasting rooms</li>
                    <li>Home gyms and wellness spaces</li>
                    <li>Guest houses and staff quarters</li>
                    <li>Smart home technology and security systems</li>
                </ul>
                
                <h4>Privacy and Security</h4>
                <p>High-end buyers prioritize privacy and security:</p>
                <ul>
                    <li>Gated communities or private estates</li>
                    <li>Advanced security systems</li>
                    <li>Landscaping that provides natural privacy</li>
                    <li>Separate entrances for staff and deliveries</li>
                    <li>Underground parking and hidden garages</li>
                </ul>
                
                <h4>Quality and Craftsmanship</h4>
                <p>Luxury buyers expect the highest quality:</p>
                <ul>
                    <li>Premium materials throughout</li>
                    <li>Attention to detail in every finish</li>
                    <li>Custom millwork and built-ins</li>
                    <li>High-end appliances and fixtures</li>
                    <li>Professional landscaping and outdoor features</li>
                </ul>
                
                <h4>Technology Integration</h4>
                <p>Modern luxury homes must include cutting-edge technology:</p>
                <ul>
                    <li>Smart home automation systems</li>
                    <li>Integrated audio/visual systems</li>
                    <li>Climate control and energy management</li>
                    <li>Security and surveillance systems</li>
                    <li>High-speed internet and connectivity</li>
                </ul>
                
                <h4>Investment Considerations</h4>
                <p>Luxury real estate is often viewed as an investment:</p>
                <ul>
                    <li>Historical appreciation in prime locations</li>
                    <li>Portfolio diversification</li>
                    <li>Potential for rental income</li>
                    <li>Tax benefits and estate planning</li>
                    <li>Hedge against inflation</li>
                </ul>
                
                <h4>Working with Luxury Buyers</h4>
                <p>Luxury real estate transactions require specialized expertise:</p>
                <ul>
                    <li>Discretion and confidentiality</li>
                    <li>Understanding of unique financing options</li>
                    <li>Access to off-market properties</li>
                    <li>International buyer considerations</li>
                    <li>Complex transaction structures</li>
                </ul>
                
                <h4>Market Trends</h4>
                <p>Current trends in luxury real estate include:</p>
                <ul>
                    <li>Increased demand for wellness-focused amenities</li>
                    <li>Growing interest in sustainable and eco-friendly features</li>
                    <li>Desire for flexible living spaces</li>
                    <li>Integration of indoor and outdoor living</li>
                    <li>Focus on health and safety features</li>
                </ul>
                
                <p>Whether buying or selling luxury real estate, working with experienced professionals who understand this unique market is essential for success.</p>
                '''
            }
        ]
        
        # Find the specific blog post
        post = None
        for p in posts:
            if p['id'] == tracking.blog_post_id:
                post = p
                break
        
        if not post:
            return HttpResponse("Blog post not found", status=404)
        
        # Get related posts (exclude current post)
        related_posts = [p for p in posts if p['id'] != tracking.blog_post_id][:2]
        
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
