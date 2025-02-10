from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if username[0] == 'M':
                login(request, user)
                return redirect('home')
            elif username[0] == 'F':
                login(request, user)
                return redirect('home:finance_home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
        
    return render(request, "login/login_page.html")
