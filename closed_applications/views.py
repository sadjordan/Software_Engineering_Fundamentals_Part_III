from django.shortcuts import render
from home.models import Application

def closed_applications_view(request):
    applications = Application.objects.all()  # Fetch applications from DB
    return render(request, "closed_applications/closed_applications_page.html", {"applications": applications})