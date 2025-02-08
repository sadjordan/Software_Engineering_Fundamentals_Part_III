from Login.models import User
from django.shortcuts import render, get_object_or_404, redirect

def user_management_view(request):
    users = User.objects.all()
    return render(request, "user_management/user_management_page.html", {"users" : users})