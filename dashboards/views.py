from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from courses.models import Course

@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related("course")
    return render(request, "dashboards/student_dashboard.html", {"enrollments": enrollments})

@login_required
def instructor_dashboard(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, "dashboards/instructor_dashboard.html", {"courses": courses})

@login_required
def sponsor_dashboard(request):
    return render(request, "dashboards/sponsor_dashboard.html")

@login_required
def admin_dashboard(request):
    stats = {
        "courses_count": Course.objects.count(),
        "enrollments_count": Enrollment.objects.count(),
    }
    return render(request, "dashboards/admin_dashboard.html", {"stats": stats})
