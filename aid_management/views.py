from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import AidRecipients

def aid_management_view(request):
    aid_recipients = AidRecipients.objects.all()  # Fetch applications from DB
    return render(request, "aid_management/aid_management_page.html", {"aid_recipients": aid_recipients})

def view_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    return render(request, 'aid_management/view_aid.html', {'aid': aid})

def suspend_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Suspended'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.save()
    return redirect('view_aid', aid_id=aid_id)

def cancel_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Cancelled'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.save()
    return redirect('view_aid', aid_id=aid_id)

def conclude_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Concluded'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.save()
    return redirect('view_aid', aid_id=aid_id)