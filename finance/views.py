from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from home.models import Application

@login_required
def finance_view_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    
    return render(request, "finance/finance_view_application.html", {"application": application})

@login_required
def approve_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.app_status = "Approved"
    application.app_decider = request.user.userid
    application.save()
    return redirect('view_application', app_id=app_id)

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
        return redirect("view_application", app_id=app_id)

    return redirect("view_application", app_id=app_id)

@login_required
def forward_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.forwarded_to_finance = True
    application.save()
    return redirect('view_application', app_id=app_id)

@login_required
def return_to_previous_page(request, app_id):
    return redirect("home:finance_home")