# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Make the login page the root
    path('', views.signup_view, name='signup'),  # Make the login page the root
]
