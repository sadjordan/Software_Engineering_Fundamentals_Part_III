from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from home.models import Application
from django.contrib import messages
from aid_management.models import AidRecipients
from view_application.forms import AidRecipientForm
from .models import FinanceInformation
from decimal import Decimal

@login_required
def finance_view_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    
    return render(request, "finance/finance_view_application.html", {"application": application})

@login_required
def approve_applicant_finance_consideration(request, app_id):
    finance_info = FinanceInformation.objects.last()
    projected_aid_needed = 10000  

    return render(request, "finance/approveApplicant.html", {
        "finance_info": finance_info,
        "projected_aid_needed": projected_aid_needed,
        "application": get_object_or_404(Application, app_id=app_id)
    })

@login_required
def approve_application(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    application.app_status = "Approved"
    application.app_decider = request.user.userid
    application.save()

    messages.success(request, "Application approved successfully.")
    
    return redirect('approve_applicant_finance_consideration', app_id=app_id)

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
        return redirect("finance_view_application", app_id=app_id)

    return redirect("finance_view_application", app_id=app_id)

@login_required
def create_aid_recipient(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)
    finance_info = FinanceInformation.objects.last()
    form = AidRecipientForm()

    count = AidRecipients.objects.count() + 1 
    new_aid_id = f"AID{count:07d}"

    if request.method == 'POST':
        projected_aid_needed = request.POST.get("projected_aid_needed", 0)
        print("Raw projected aid needed:", projected_aid_needed)
        # projected_aid_needed = Decimal(projected_aid_needed)

        # if projected_aid_needed:
        #     try:
        #         projected_aid_needed = Decimal(projected_aid_needed)
        #     except:
        #         print("nope")
        #         projected_aid_needed = Decimal("0.00")
        # else:
        #     projected_aid_needed = Decimal("0.00")

        # print("Final Decimal aid needed:", projected_aid_needed)
        old = finance_info.total_aid_balance
        finance_info.total_aid_balance -= projected_aid_needed
        finance_info.save()

        form = AidRecipientForm(request.POST)
        if form.is_valid():
            aid_recipient = form.save(commit=False)
            aid_recipient.app = application
            aid_recipient.user_id = application.user_id
            aid_recipient.aid_id = new_aid_id
            aid_recipient.save()
            return redirect('home:finance_home')

    context = {'form': form, 'application': application, 'aid_id': new_aid_id}
    return render(request, 'view_application/create_aid_recipient.html', context)


@login_required
def return_to_previous_page(request, app_id):
    return redirect("home:finance_home")

def request_more_budget(request):
    return render(request, 'finance/requestForm.html')