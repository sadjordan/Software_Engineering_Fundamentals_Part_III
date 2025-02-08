from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_management_view, name='user_management')
]