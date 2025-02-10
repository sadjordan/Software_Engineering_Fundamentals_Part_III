from django.urls import path
from .views import * # Import your view

urlpatterns = [
    # path('<str:app_id>/', finance_view_application, name='view_application'),
    path('view_application/<str:app_id>/', finance_view_application, name='finance_view_application'),
    path('<str:app_id>/approve/', approve_application, name='approve_application'),
    path('<str:app_id>/deny/', deny_application, name='deny_application'),
    path('<str:app_id>/forward/', forward_application, name='forward_application'),
    path('<str:app_id>/return/', return_to_previous_page, name='close'),
]
