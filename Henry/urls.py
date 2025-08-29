from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('featured_properties/', views.featured_properties, name='featured_properties'),
    path('blog/', views.blog, name='blog'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('buying/', views.buying, name='buying'),
    path('selling/', views.selling, name='selling'),
    path('leasing/', views.leasing, name='leasing'),
    path('home-valuation/', views.home_valuation, name='home_valuation'),
    path('open-house/', views.open_house, name='open_house'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage_calculator'),
    path('market-insights/', views.market_insights, name='market_insights'),
]
