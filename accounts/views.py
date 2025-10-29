from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def welcome(request):
    
    return render(request, "accounts/welcome.html")

@login_required
def profile(request):

    return render(request, "accounts/profile.html")

def logout_view(request):
    
    logout(request)
    return redirect("welcome")
