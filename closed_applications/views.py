from django.shortcuts import render, get_object_or_404
from home.models import Application

def closed_applications_view(request):
    closed_applications = Application.objects.filter(app_status="Approved" or "Denied")
    return render(request, "closed_applications/closed_applications_page.html", {"applications": closed_applications})

def view_report_view(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    return render(request, 'closed_applications/view_report_page.html', {'application': application})
