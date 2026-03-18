"""Defines url patterns for account"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
]