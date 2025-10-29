from .models import Notification

def create_notification_for_user(user, message):
    Notification.objects.create(user=user, message=message)
