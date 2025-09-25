from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('featured_properties/', views.featured_properties, name='featured_properties'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('buy-lease/', views.buy_lease, name='buy_lease'),
    path('buying/', views.buying, name='buying'),
    path('selling/', views.selling, name='selling'),
    path('leasing/', views.leasing, name='leasing'),
    # path('home-valuation/', views.home_valuation, name='home_valuation'),  # Commented out - functionality moved to selling page
    path('open-house/', views.open_house, name='open_house'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage_calculator'),
    path('market-insights/', views.market_insights, name='market_insights'),
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
]
