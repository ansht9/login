from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirects the root URL to the login page
    path('', lambda request: redirect('signup')),
    path('login/', include('accounts.urls')),  # The login URL
    path('signup/', include('accounts.urls')),  # The login URL
]
