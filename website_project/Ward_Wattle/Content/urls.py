from django.contrib import admin
from django.urls import path, include
from . import views
from .views import emailView, successView

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('aboutus', views.aboutus.as_view(), name='aboutus'),
    path('policy', views.policy.as_view(), name='policy'),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]
