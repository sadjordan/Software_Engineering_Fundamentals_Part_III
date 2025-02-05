from django.urls import path
from .views import view_application_view  # Import your view

urlpatterns = [
    path('<str:app_id>/', view_application_view, name='view_application'),
]
