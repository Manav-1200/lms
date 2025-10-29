from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Subject, Sector, Assignment
from enrollments.models import Enrollment
from django.contrib import messages

@login_required
def course_list(request):
    # show all courses with basic related fields to look simple but clear
    courses = Course.objects.select_related("subject", "instructor").all()
    return render(request, "courses/course_list.html", {"courses": courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # check enrollment status
    enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    # show assignments to enrolled students and instructors
    assignments = Assignment.objects.filter(course=course).order_by("-created_at")
    return render(request, "courses/course_detail.html", {"course": course, "enrolled": enrolled, "assignments": assignments})
