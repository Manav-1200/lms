from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username in API

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'created_at', 'read']
