from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()


def welcome(request):
    return render(request, "accounts/welcome.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user and redirect to login
            user = form.save()
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect("accounts:login")
        else:
            messages.error(request, "Something went wrong. Please check the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")

            # Redirect to the correct dashboard based on role
            role = getattr(user, "role", None) or ("admin" if user.is_superuser else "student")
            if role == "admin":
                return redirect("dashboards:admin_dashboard")
            elif role == "instructor":
                return redirect("dashboards:instructor_dashboard")
            elif role == "student":
                return redirect("dashboards:student_dashboard")
            elif role == "sponsor":
                return redirect("dashboards:sponsor_dashboard")
            else:
                return redirect("accounts:welcome")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    # Logs out the user and redirects to the home (welcome) page.
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("welcome")


@login_required
def profile_view(request):
    # Displays simple profile info for the logged-in user.
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def dashboard(request):
    # Dashboard view for logged-in users. Displays basic information like enrolled courses, notifications, etc.
    # The role is also shown.
    user = request.user
    role = getattr(user, "role", None) or ("admin" if user.is_superuser else "student")

    enrolled_count = 0
    total_courses = 0
    notifications_count = 0

    try:
        from enrollments.models import Enrollment
        from courses.models import Course
        from notifications.models import Notification
    except Exception:
        Enrollment, Course, Notification = None, None, None

    try:
        if Enrollment:
            enrolled_count = Enrollment.objects.filter(student=user).count()
        if Course:
            total_courses = Course.objects.count()
        if Notification:
            notifications_count = Notification.objects.filter(user=user, read=False).count()
    except Exception:
        pass  # safely ignore errors

    context = {
        "user": user,
        "role": role,
        "is_admin": user.is_superuser,
        "is_instructor": role == "instructor",
        "is_student": role == "student",
        "is_sponsor": role == "sponsor",
        "enrolled_count": enrolled_count,
        "total_courses": total_courses,
        "notifications_count": notifications_count,
    }

    return render(request, "accounts/dashboard.html", context)
