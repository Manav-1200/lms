from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .models import Enrollment
from notifications.utils import create_notification_for_user

@login_required
def enroll_in_course(request, course_pk):
    """
    Endpoint to enroll the logged-in user in the given course.
    Requires POST so users cannot accidentally enroll via link GET.
    """
    if request.method != "POST":
        messages.error(request, "Use the 'Enroll' button on the course page to enroll.")
        return redirect("courses:course_detail", pk=course_pk)

    course = get_object_or_404(Course, pk=course_pk)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    if created:
        # mark payment as completed if price is zero or simulate payment success
        if course.price and float(course.price) > 0:
            enrollment.payment_completed = True
            enrollment.save()
        # send a notification to user
        try:
            create_notification_for_user(request.user, f"You are now enrolled in {course.title}.")
        except Exception:
            # don't crash the site if notifications fail — show message instead
            pass
        messages.success(request, f"You have been enrolled in {course.title}.")
    else:
        messages.info(request, "You are already enrolled in this course.")

    return redirect("courses:course_detail", pk=course_pk)
