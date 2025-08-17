import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from notifications.utils import notify_user
from enrollments.models import Submission
from courses.models import Assessment

# Notify student when submission is graded
@receiver(post_save, sender=Submission)
def notify_on_grade(sender, instance, created, **kwargs):
    if not created:
        notify_user(
            recipient=instance.enrollment.student,
            title=f"Assessment graded: {instance.assessment.title}",
            message=f"Your score: {instance.score}/{instance.assessment.max_score}"
        )

# Notify students 24h before assessment due date
@receiver(post_save, sender=Assessment)
def schedule_due_soon_notification(sender, instance, created, **kwargs):
    if instance.due_date:
        hours_until_due = (instance.due_date - timezone.now()).total_seconds() / 3600
        if 0 < hours_until_due <= 24:
            enrollments = instance.course.enrollments.select_related("student")
            for e in enrollments:
                notify_user(
                    recipient=e.student,
                    title=f"Assessment due soon: {instance.title}",
                    message="This is a reminder: your assessment is due within 24 hours."
                )
