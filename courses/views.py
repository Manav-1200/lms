from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Sector, Subject, Course
from enrollments.models import Enrollment

def sector_list(request):
    
    # Show all sectors publicly. Anyone can view sectors.
   
    sectors = Sector.objects.all().order_by("name")
    return render(request, "courses/sector_list.html", {"sectors": sectors})

@login_required
def course_list(request):
    
    # show latest courses first for nicer UI
    courses = Course.objects.select_related("subject", "instructor").order_by("-created_at")
    return render(request, "courses/course_list.html", {"courses": courses})

@login_required
def course_detail(request, pk):
    
    # Show a single course detail. Indicate if the user is enrolled.
    
    course = get_object_or_404(Course, pk=pk)
    enrolled = Enrollment.objects.filter(course=course, student=request.user).exists()
    return render(request, "courses/course_detail.html", {"course": course, "enrolled": enrolled})
