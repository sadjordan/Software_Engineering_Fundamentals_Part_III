from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.user_management_view, name='user_management'),
    path('create/', views.create_user_view, name='create_user_page'),
    path('create/submit/', views.create_user, name='create_user'),
    path('edit/<str:user_id>/', views.edit_user_view, name='edit_user_page'),
    path('generate_user_id/<str:user_type>/', generate_user_id, name='generate_user_id')
]