from django.core.mail import send_mail
from django.conf import settings
from .models import Notification

def notify_user(recipient, title: str, message: str, email: bool = True, in_app: bool = True):
    if in_app:
        Notification.objects.create(recipient=recipient, title=title, message=message)
    if email and recipient.email:
        send_mail(
            subject=title,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient.email],
            fail_silently=True,
        )
