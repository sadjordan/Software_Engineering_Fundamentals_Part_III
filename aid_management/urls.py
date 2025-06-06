from django.urls import path

from . import views

urlpatterns = [
    path('', views.aid_management_view, name='aid_management'),
    path('aid/<str:aid_id>/', views.view_aid, name='view_aid'),
    path('aid/<str:aid_id>/suspend/', views.suspend_aid, name='suspend_aid'),
    path('aid/<str:aid_id>/cancel/', views.cancel_aid, name='cancel_aid'),
    path('aid/<str:aid_id>/conclude/', views.conclude_aid, name='conclude_aid'),
]