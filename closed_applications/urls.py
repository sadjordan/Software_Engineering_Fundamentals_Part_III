from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.closed_applications_view, name='closed_applications'),
    path('<str:app_id>/', views.view_report_view, name='view_report'),
]