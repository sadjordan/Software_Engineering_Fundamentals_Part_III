from django.shortcuts import render
from home.models import Application

def aid_management_view(request):
    applications = Application.objects.all()  # Fetch applications from DB
    return render(request, "aid_management/aid_management_page.html", {"applications": applications})