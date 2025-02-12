from django.shortcuts import render, get_object_or_404, redirect
from home.models import Application
from aid_management.models import AidRecipients
from .forms import AidRecipientForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def view_application_view(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    return render(request, 'view_application/view_application_page.html', {'application': application})

@login_required
def approve_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)

    if request.method == 'POST':
        application.app_status = 'Approved'
        application.app_decider = request.user.userid
        application.save()
        messages.success(request, "Application approved successfully.")
        return redirect('create_aid_recipient', app_id=app_id)  # Redirecting to create aid recipient

    return redirect('home')

@login_required
def deny_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)

    if request.method == "POST":
        change_reason = request.POST.get("change_reason", "").strip()

        # if not change_reason:
        #     messages.error(request, "Denial reason is required.")
        #     return redirect("view_application", app_id=app_id)

        application.app_status = "Denied"
        application.app_denyreason = change_reason
        application.app_decider = request.user.userid
        application.save()
        messages.success(request, "Application denied successfully.")
        return redirect("view_application", app_id=app_id)

    return redirect("view_application", app_id=app_id)

@login_required
def forward_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.forwarded_to_finance = True
    application.save()
    messages.success(request, "Application forwarded successfully.")
    return redirect('view_application', app_id=app_id)

@login_required
def return_to_previous_page(request, app_id):
    return redirect("home")


@login_required
def create_aid_recipient(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    form = AidRecipientForm()

    count = AidRecipients.objects.count() + 1 
    new_aid_id = f"AID{count:07d}"

    if request.method == 'POST':
        form = AidRecipientForm(request.POST)
        if form.is_valid():
            aid_recipient = form.save(commit=False)
            aid_recipient.app = application
            aid_recipient.user_id = application.user_id
            aid_recipient.aid_id = new_aid_id
            aid_recipient.save()
            return redirect('home:home')

    context = {'form': form, 'application': application, 'aid_id': new_aid_id}
    return render(request, 'view_application/create_aid_recipient.html', context)
