from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .models import Enrollment
from notifications.utils import create_notification_for_user

@login_required
def enroll_in_course(request, course_pk):
    # Accept POST only to avoid accidental enrollments via GET
    if request.method != "POST":
        messages.error(request, "Please use the enroll button on the course page.")
        return redirect("courses:course_detail", pk=course_pk)

    course = get_object_or_404(Course, pk=course_pk)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    if created:
        # Just for the demo, we'll pretend payment is always successful if price > 0
        if course.price and course.price > 0:
            enrollment.payment_completed = True
            enrollment.save()
        # create a simple notification for the student
        create_notification_for_user(request.user, f"You have enrolled in {course.title}.")
        messages.success(request, f"Enrolled in {course.title}.")
    else:
        messages.info(request, f"You are already enrolled in {course.title}.")

    return redirect("courses:course_detail", pk=course_pk)
