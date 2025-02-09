from django.shortcuts import render, get_object_or_404
from .models import AidRecipients

def aid_management_view(request):
    aid_recipients = AidRecipients.objects.all()  # Fetch applications from DB
    return render(request, "aid_management/aid_management_page.html", {"aid_recipients": aid_recipients})

def view_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    return render(request, 'aid_management/view_aid.html', {'aid': aid})