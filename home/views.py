from .models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from aid_management.models import AidRecipients
from finance.models import FinanceInformation


@login_required
def home_view(request):
    pending_applications = Application.objects.filter(app_status="Pending")
    return render(request, "home/management_home_page.html", {"applications": pending_applications})

@login_required
def finance_home(request):
    applications = Application.objects.filter(forwarded_to_finance=True)
    aid_mapping = {aid.app_id: aid.aid_id for aid in AidRecipients.objects.all()}
    applications_with_aids = [
        {
            'app_id': application.app_id,
            'user_id': application.user_id,
            'app_type': application.app_type,
            'app_date': application.app_date,
            'app_status': application.app_status,
            'aid_id': aid_mapping.get(application.app_id),
        }
        for application in applications
    ]

    finance_info = FinanceInformation.objects.last()
    current_sem_budget = finance_info.current_sem_budget
    total_aid_balance = finance_info.total_aid_balance
    projected_aid_needed = current_sem_budget - total_aid_balance

    context = {
        'applications': applications_with_aids,
        'current_sem_budget': current_sem_budget,
        'total_aid_balance': total_aid_balance,
        'projected_aid_needed': projected_aid_needed,
    }

    return render(request, 'home/finance_home_page.html', context)

