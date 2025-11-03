from django.db.models.signals import post_save
from django.dispatch import receiver
from enrollments.models import Enrollment
from .utils import create_notification_for_user

@receiver(post_save, sender=Enrollment)
def send_enrollment_notification(sender, instance, created, **kwargs):
    # When new enrollment is created, send notification
    if created:
        try:
            create_notification_for_user(instance.student, f"You were enrolled in {instance.course.title}.")
        except Exception:
            # avoid raising in signal
            pass
