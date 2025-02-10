from Login.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password 
from django.contrib import messages
from home.models import Application
from django.http import JsonResponse
from .models import UserIDTracker
from django.contrib.auth.decorators import login_required


@login_required
def generate_user_id(request, user_type):
    if user_type not in ["M", "F", "S", "U"]:
        return JsonResponse({"error": "Invalid user type"}, status=400)

    tracker, created = UserIDTracker.objects.get_or_create(category=user_type)
    tracker.last_number += 1
    tracker.save()

    new_user_id = f"{user_type}{tracker.last_number:09d}"

    return JsonResponse({"user_id": new_user_id})

@login_required
def user_management_view(request):
    users = User.objects.all()
    return render(request, "user_management/user_management_page.html", {"users" : users})

@login_required
def create_user_view(request):
    return render(request, 'user_management/create_user_page.html', {'user': None})

@login_required
def edit_user_view(request, user_id):
    user = get_object_or_404(User, userid=user_id)

    return render(request, 'user_management/create_user_page.html', {'user': user, 'edit_mode': True})

@login_required
def create_user(request):
    if request.method == 'POST':
        original_userid = request.POST.get('original_userid')
        new_userid = request.POST.get('userid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        if original_userid:
            try:
                user = User.objects.get(userid=original_userid)

                if original_userid != new_userid and User.objects.filter(userid=new_userid).exists():
                    messages.error(request, "New User ID already exists. Choose another.")
                    return redirect('create_user_page')

                user.userid = new_userid  # Change user ID
                user.first_name = first_name
                user.last_name = last_name
                if password:  # Only update password if provided
                    user.password = make_password(password)
                user.save()
                Application.objects.filter(user=original_userid).update(user=new_userid)

                messages.success(request, "User updated successfully!")

            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('user_management')  # Redirect back

        else:  # If creating a new user
            if not new_userid:  # Prevent empty user ID
                messages.error(request, "User ID cannot be empty.")
                return redirect('create_user_page')
            
            if User.objects.filter(userid=new_userid).exists():
                messages.error(request, "User ID already exists.")
                return redirect('create_user_page')

            user = User(userid=new_userid, first_name=first_name, last_name=last_name, password=make_password(password))
            user.save()
            messages.success(request, "User created successfully!")

        return redirect('user_management')

    return redirect('create_user_page')
