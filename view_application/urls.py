from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_application_view, name='view_application')
]