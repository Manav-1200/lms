from django.db.models.signals import post_save
from django.dispatch import receiver
from enrollments.models import Enrollment
from .utils import create_notification_for_user

@receiver(post_save, sender=Enrollment)
def enrollment_created(sender, instance, created, **kwargs):
    # When a new enrollment is created it send a notification
    if created:
        user = instance.student
        course_title = instance.course.title
        create_notification_for_user(user, f"You are now enrolled in {course_title}.")
