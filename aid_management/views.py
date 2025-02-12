from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import AidRecipients

@login_required
def aid_management_view(request):
    aid_recipients = AidRecipients.objects.all()
    return render(request, "aid_management/aid_management_page.html", {"aid_recipients": aid_recipients})


@login_required
def view_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    is_finance_user = False
    
    if request.user.userid[0] == 'F':
        is_finance_user = True

    context = {
        "aid": aid,
        "is_finance_user": is_finance_user,
    }
    return render(request, 'aid_management/view_aid.html', context)

@login_required
def suspend_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Suspended'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.aid_changedecider = request.user.userid
        aid.save()
    return redirect('view_aid', aid_id=aid_id)

@login_required
def cancel_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Cancelled'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.aid_changedecider = request.user.userid
        aid.save()
    return redirect('view_aid', aid_id=aid_id)

@login_required
def conclude_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Concluded'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.aid_changedecider = request.user.userid
        aid.save()
    return redirect('view_aid', aid_id=aid_id)

@login_required
def update_aid_description(request, aid_id):
    if request.method == 'POST':
        aid = get_object_or_404(AidRecipients, aid_id=aid_id)
        aid.aid_desc = request.POST.get('aid_description', aid.aid_desc)
        aid.save()
        return redirect('view_aid', aid_id=aid_id)
    return redirect('view_aid', aid_id=aid_id)

@login_required
def continue_aid(request, aid_id):
    aid = get_object_or_404(AidRecipients, aid_id=aid_id)
    if request.method == 'POST':
        aid.aid_status = 'Ongoing'
        aid.aid_changereason = request.POST.get('aid_changereason')
        aid.aid_changedate = timezone.now().date()
        aid.aid_changedecider = request.user.userid
        aid.save()
    return redirect('view_aid', aid_id=aid_id)