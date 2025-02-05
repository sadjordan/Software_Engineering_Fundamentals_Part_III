from django.urls import path

from . import views

urlpatterns = [
    path('', views.closed_applications_view, name='closed_applications')
]