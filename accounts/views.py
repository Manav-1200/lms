from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def welcome(request):
    return render(request, "accounts/welcome.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("role_redirect")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def role_redirect(request):
    role = request.user.role
    if role == "student":
        return redirect("student_dashboard")
    elif role == "instructor":
        return redirect("instructor_dashboard")
    elif role == "sponsor":
        return redirect("sponsor_dashboard")
    elif role == "admin":
        return redirect("admin_dashboard")
    return redirect("welcome")
