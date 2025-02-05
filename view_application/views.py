from django.shortcuts import render
from home.models import Application

def view_application_view(request):
    applications = Application.objects.all()  # Fetch applications from DB
    return render(request, "view_application/view_application_page.html", {"applications": applications})
