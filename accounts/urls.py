# accounts/urls.py
"""Defines URL patterns for accounts."""
from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # Include default auth URLs.
    path('', include('django.contrib.auth.urls')),  # This includes login, logout, password reset URLs, etc.
    path('register/', views.register, name='register')
]
