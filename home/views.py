from .models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from aid_management.models import AidRecipients
from finance.models import FinanceInformation
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from home.models import Application
import io


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
            'Financial_aid_status' : application.Financial_aid_status,
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

@login_required
def view_pdf(request, app_id):
    application = get_object_or_404(Application, app_id=app_id)

    if application.app_attached1:
        pdf_data = application.app_attached1  # BinaryField
        print(f"✅ PDF found for {app_id}, Size: {len(pdf_data)} bytes")

        # Convert BinaryField data to BytesIO
        pdf_file = io.BytesIO(pdf_data)  
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="document.pdf"'
        return response

    print("❌ No PDF found")
    return HttpResponse("Error: No PDF found", status=404)

@csrf_exempt  # Remove this if using CSRF protection
@require_POST
def update_application_status(request, app_id):
    try:
        data = json.loads(request.body)
        new_status = data.get("status")

        application = Application.objects.get(app_id=app_id)
        application.Financial_aid_status = new_status
        application.save()

        return JsonResponse({"success": True, "new_status": new_status})
    except Application.DoesNotExist:
        return JsonResponse({"success": False, "error": "Application not found."}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)