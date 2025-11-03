from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Landing / welcome page
def welcome(request):
    """
    Public landing page. Shows login/register if not logged in,
    and a link to dashboard/profile if logged in.
    """
    return render(request, "accounts/welcome.html")


# Login view (simple)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("accounts:dashboard")  # land on dashboard after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# Register view (simple)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("accounts:login")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# Profile view (simple)
@login_required
def profile_view(request):
    """
    Basic profile page. Shows basic info about the logged-in user.
    """
    return render(request, "accounts/profile.html", {"user": request.user})


# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("welcome")


# Dashboard view (role-aware, beginner-friendly)
@login_required
def dashboard(request):
    """
    Simple dashboard that shows counts and small summaries.
    """
    user = request.user

    # defaults
    enrolled_count = 0
    total_courses = 0
    notifications_count = 0

    # Import here to avoid circular import at module load (safer)
    try:
        from enrollments.models import Enrollment
        from courses.models import Course
        from notifications.models import Notification
    except Exception:
        Enrollment = None
        Course = None
        Notification = None

    # compute enrolled courses count (if enrollments app is present)
    try:
        if Enrollment is not None:
            enrolled_count = Enrollment.objects.filter(student=user).count()
    except Exception:
        enrolled_count = 0

    # compute total courses (if courses app is present)
    try:
        if Course is not None:
            total_courses = Course.objects.count()
    except Exception:
        total_courses = 0

    # compute notifications count (if notifications app is present)
    try:
        if Notification is not None:
            notifications_count = Notification.objects.filter(user=user, read=False).count()
    except Exception:
        notifications_count = 0

    # role flags for template to show role-specific shortcuts
    role = getattr(user, "role", None) or ( "admin" if user.is_superuser else "student" )
    is_admin = role == "admin" or user.is_superuser
    is_instructor = role == "instructor"
    is_student = role == "student"
    is_sponsor = role == "sponsor"

    context = {
        "user": user,
        "role": role,
        "is_admin": is_admin,
        "is_instructor": is_instructor,
        "is_student": is_student,
        "is_sponsor": is_sponsor,
        "enrolled_count": enrolled_count,
        "total_courses": total_courses,
        "notifications_count": notifications_count,
    }

    return render(request, "accounts/dashboard.html", context)
