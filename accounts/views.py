from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def welcome(request):
  
    # Landing page for visitors. 
    # Shows 'Login' and 'Register' buttons for unauthenticated users,or redirects to dashboard if logged in.
   
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    return render(request, "accounts/welcome.html")


def login_view(request):
   
    # Basic login view with error messages.
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
   
    # Registration page for new users 
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("accounts:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    
    # Displays user information
    
    user = request.user
    context = {"user": user}
    return render(request, "accounts/profile.html", context)


@login_required
def logout_view(request):
    """
    Logs out the current user and redirects to welcome page.
    """
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect("welcome")


@login_required
def dashboard(request):
   
    # Dashboard page that shows corresponding data depending on the user role
    
    user = request.user

    # Safe imports
    try:
        from enrollments.models import Enrollment
        from courses.models import Course
        from notifications.models import Notification
    except Exception:
        Enrollment = Course = Notification = None

    # Default counters
    total_courses = 0
    enrolled_count = 0
    my_courses = []
    my_notifications = []

    # Count and display data 
    try:
        if Course:
            total_courses = Course.objects.count()
            if hasattr(user, "role") and user.role == "instructor":
                my_courses = Course.objects.filter(instructor=user)
        if Enrollment and hasattr(user, "role") and user.role == "student":
            enrolled_count = Enrollment.objects.filter(student=user).count()
        if Notification:
            my_notifications = Notification.objects.filter(user=user).order_by("-created_at")[:5]
    except Exception:
        pass  

    # Detect role
    role = getattr(user, "role", "student")
    if user.is_superuser:
        role = "admin"

    context = {
        "user": user,
        "role": role,
        "total_courses": total_courses,
        "enrolled_count": enrolled_count,
        "my_courses": my_courses,
        "my_notifications": my_notifications,
    }

    return render(request, "accounts/dashboard.html", context)
