from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('featured_properties/', views.featured_properties, name='featured_properties'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('buy-lease/', views.buy_lease, name='buy_lease'),
    path('community/<slug:slug>/', views.community_detail, name='community_detail'),
    path('buying/', views.buying, name='buying'),
    path('selling/', views.selling, name='selling'),
    path('leasing/', views.leasing, name='leasing'),
    # path('home-valuation/', views.home_valuation, name='home_valuation'),  # Commented out - functionality moved to selling page
    path('open-house/', views.open_house, name='open_house'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage_calculator'),
    path('market-insights/', views.market_insights, name='market_insights'),
    path('api/property/<int:property_id>/', views.get_property_details, name='property_api'),
    path('debug-images/', views.debug_images, name='debug_images'),
    path('debug-blog-image/<int:post_id>/', views.debug_blog_image, name='debug_blog_image'),
    path('debug-open-house-images/<int:open_house_id>/', views.debug_open_house_images, name='debug_open_house_images'),
    # Inquiry form URLs
    path('property-inquiry/', views.property_inquiry, name='property_inquiry'),
    path('mortgage-inquiry/', views.mortgage_inquiry, name='mortgage_inquiry'),
    # Blog tracking URLs
    path('tracked-blog/<uuid:tracking_code>/', views.tracked_blog_detail, name='tracked_blog_detail'),
    path('api/create-tracking-link/', views.create_tracking_link, name='create_tracking_link'),
    path('tracking-dashboard/', views.tracking_dashboard, name='tracking_dashboard'),

    # Blog admin URLs (moved to avoid conflict with Django admin)
    path('blog-admin/', views.blog_admin, name='blog_admin'),
    path('blog-admin/add/', views.blog_add, name='blog_add'),
    path('blog-admin/edit/<int:post_id>/', views.blog_edit, name='blog_edit'),
    path('blog-admin/delete/<int:post_id>/', views.blog_delete, name='blog_delete'),

    # Legal pages
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),

    # New tracking URL patterns (must be after all other patterns)
    # Blog tracking: /blog/<post_id>/u-<customer_code>/
    path('blog/<int:post_id>/u-<str:customer_code>/', views.tracked_blog_detail_new, name='tracked_blog_detail_new'),
    path('blog/<int:post_id>/u-<str:customer_code>', views.tracked_blog_detail_new),
    # Blog root tracking
    path('blog/u-<str:customer_code>/', views.tracked_blog_root, name='tracked_blog_root'),
    path('blog/u-<str:customer_code>', views.tracked_blog_root),

    # Page tracking with customer codes: /<page>/u-<customer_code>/
    path('open-house/u-<str:customer_code>/', views.tracked_open_house, name='tracked_open_house'),
    path('open-house/u-<str:customer_code>', views.tracked_open_house),
    path('api/open-house/<int:open_house_id>/', views.get_open_house_details, name='open_house_api'),
    path('selling/u-<str:customer_code>/', views.tracked_selling, name='tracked_selling'),
    path('selling/u-<str:customer_code>', views.tracked_selling),
    path('buy-lease/u-<str:customer_code>/', views.tracked_buy_lease, name='tracked_buy_lease'),
    path('buy-lease/u-<str:customer_code>', views.tracked_buy_lease),
    path('mortgage-calculator/u-<str:customer_code>/', views.tracked_mortgage_calculator,
         name='tracked_mortgage_calculator'),
    path('mortgage-calculator/u-<str:customer_code>', views.tracked_mortgage_calculator),

    # Legal pages tracking
    path('terms-of-service/u-<str:customer_code>/', views.tracked_terms, name='tracked_terms'),
    path('terms-of-service/u-<str:customer_code>', views.tracked_terms),
    path('privacy-policy/u-<str:customer_code>/', views.tracked_privacy, name='tracked_privacy'),
    path('privacy-policy/u-<str:customer_code>', views.tracked_privacy),
    path('cookie-policy/u-<str:customer_code>/', views.tracked_cookie, name='tracked_cookie'),
    path('cookie-policy/u-<str:customer_code>', views.tracked_cookie),

    # General tracking: /u-<customer_code>/
    path('u-<str:customer_code>/', views.general_tracking_redirect, name='general_tracking_redirect'),
    path('u-<str:customer_code>', views.general_tracking_redirect),
]
