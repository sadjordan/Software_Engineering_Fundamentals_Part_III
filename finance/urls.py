from django.urls import path
from .views import * # Import your view

urlpatterns = [
    # path('<str:app_id>/', finance_view_application, name='view_application'),
    path('view_application_finance/<str:app_id>/', finance_view_application, name='finance_view_application'),
    path('<str:app_id>/approve/', approve_application, name='finance_approve_application'),
    path('<str:app_id>/deny/', deny_application, name='finance_deny_application'),
    path('<str:app_id>/forward/', forward_application, name='finance_forward_application'),
    path('<str:app_id>/return/', return_to_previous_page, name='finance_close'),
]
