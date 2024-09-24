from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_device, name='search_device'),
    path('api/search/', views.api_search_device, name='api_search_device'),
]   