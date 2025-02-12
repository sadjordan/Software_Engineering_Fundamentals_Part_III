from django.urls import path
from .views import * # Import your view

urlpatterns = [
    # path('<str:app_id>/', finance_view_application, name='view_application'),
    path('view_application_finance/<str:app_id>/', finance_view_application, name='finance_view_application'),
    path('<str:app_id>/approve/', approve_application, name='finance_approve_application'),
    path('<str:app_id>/deny/', deny_application, name='finance_deny_application'),
    path('<str:app_id>/return/', return_to_previous_page, name='finance_close'),
    path("finance/<str:app_id>/approve/", approve_applicant_finance_consideration, name="approve_applicant_finance_consideration"),
    path('<str:app_id>/finance_create_aid_recipient/', create_aid_recipient, name='finance_create_aid_recipient'),
    path('request-budget/', request_more_budget, name='request_more_budget'),
]
