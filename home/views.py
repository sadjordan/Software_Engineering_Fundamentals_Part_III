from .models import Application
from django.shortcuts import render, get_object_or_404, redirect

def home_view(request):
    pending_applications = Application.objects.filter(app_status="Pending")
    return render(request, "home/management_home_page.html", {"applications": pending_applications})