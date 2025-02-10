from django.shortcuts import render, get_object_or_404, redirect
from home.models import Application

def view_application_view(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    return render(request, 'view_application/view_application_page.html', {'application': application})

def approve_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.app_status = "Approved"
    application.save()
    return redirect('view_application', app_id=app_id)

def deny_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)

    if request.method == "POST":
        change_reason = request.POST.get("change_reason", "").strip()

        # if not change_reason:
        #     messages.error(request, "Denial reason is required.")
        #     return redirect("view_application", app_id=app_id)

        application.app_status = "Denied"
        application.app_denyreason = change_reason
        application.save()
        return redirect("view_application", app_id=app_id)

    return redirect("view_application", app_id=app_id)

def forward_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.forwarded_to_finance = True
    application.save()
    return redirect('view_application', app_id=app_id)

def return_to_previous_page(request, app_id):
    return redirect("home")