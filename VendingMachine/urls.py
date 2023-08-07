"""
URL configuration for VendingMachine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from item import views

urlpatterns = [
    # Admin area URL.
    path('admin/', admin.site.urls),

    # Admin dashboard URL.
    path('admin/dashboard/', views.dashboard, name='dashboard'),

    # URL patterns for the 'item' app.
    path('item/', include('item.urls')),

    # If the user accesses the base URL, redirect to the 'item/' path.
    re_path(r'^$', RedirectView.as_view(url='/item/')),

]
