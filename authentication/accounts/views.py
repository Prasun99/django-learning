from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForms


def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful")
            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed")
    else:
        form = RegistrationForms()

    return render(request, 'accounts/register.html', {'form': form})


def login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'accounts/login.html')


def logout(request):   
    auth_logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')   


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')