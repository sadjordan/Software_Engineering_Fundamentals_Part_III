from django.urls import path
from .views import view_pdf
from . import views
from .views import update_application_status

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path("view-pdf/<str:app_id>/", view_pdf, name="view_pdf"),
    path('finance/', views.finance_home, name='finance_home'),
     path('update-status/<str:app_id>/', update_application_status, name='update_status'),
]