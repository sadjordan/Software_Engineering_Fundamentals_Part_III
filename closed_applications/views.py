from django.shortcuts import render
from home.models import Application

def closed_applications_view(request):
    closed_applications = Application.objects.filter(app_status="Approved" or "Denied")
    return render(request, "closed_applications/closed_applications_page.html", {"applications": closed_applications})
