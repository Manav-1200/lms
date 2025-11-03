from .models import Notification

def create_notification_for_user(user, message):
    # Simple helper — create a notification record
    if user:
        Notification.objects.create(user=user, message=message)
