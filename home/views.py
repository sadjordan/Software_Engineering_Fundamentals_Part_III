from .models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from aid_management.models import AidRecipients


@login_required
def home_view(request):
    pending_applications = Application.objects.filter(app_status="Pending")
    return render(request, "home/management_home_page.html", {"applications": pending_applications})

@login_required
def finance_home(request):
    applications = Application.objects.all()
    
    # Create a dictionary mapping app_id to aid_id
    aid_mapping = {aid.app: aid.aid_id for aid in AidRecipients.objects.all()}

    return render(request, 'finance/home.html', {
        'applications': applications,
        'aid_mapping': aid_mapping  # Pass this mapping to the template
    })

