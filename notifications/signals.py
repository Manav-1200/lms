from django.db.models.signals import post_save
from django.dispatch import receiver
from enrollments.models import Enrollment
from .models import Notification

@receiver(post_save, sender=Enrollment)
def enrollment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.student,
            message=f"You have successfully enrolled in {instance.course.title}!"
        )
