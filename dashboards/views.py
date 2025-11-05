from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, "dashboards/admin.html")

@login_required
def instructor_dashboard(request):
    return render(request, "dashboards/instructor.html")

@login_required
def student_dashboard(request):
    return render(request, "dashboards/student_dashboard.html")  # updated

@login_required
def sponsor_dashboard(request):
    return render(request, "dashboards/sponsor.html")
