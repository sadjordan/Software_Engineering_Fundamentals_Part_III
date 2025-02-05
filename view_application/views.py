from django.shortcuts import render, get_object_or_404
from home.models import Application  # Import your model

def view_application_view(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    return render(request, 'view_application/view_application_page.html', {'application': application})

