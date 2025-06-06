"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path("login/", include("Login.urls")),
    path('home/', include("home.urls")),
    path('closed-applications/', include("closed_applications.urls")),
    path('aid-management/', include("aid_management.urls")),
    path('view_application/', include('view_application.urls')),
    path('user_management/', include("user_management.urls")),
    path('finance/', include('finance.urls')),
    path('admin/', admin.site.urls)
]
