from django.urls import path

from . import views

urlpatterns = [
    path('', views.aid_management_view, name='aid_management'),
    path('aid/<str:aid_id>/', views.view_aid, name='view_aid')
]