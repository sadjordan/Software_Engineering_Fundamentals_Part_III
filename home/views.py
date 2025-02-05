from django.shortcuts import render
from .models import Application

def home_view(request):
    applications = Application.objects.all()  # Fetch applications from DB
    return render(request, "home/home_page.html", {"applications": applications})
