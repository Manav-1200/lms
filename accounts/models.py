from django.db import models
from django.contrib.auth.models import AbstractUser

# extended user model so you can assign roles.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("sponsor", "Sponsor"),
    ]
    # role field to identify users
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student", help_text="Role of the user")

    def __str__(self):
        # Show role for readability in admin lists
        return f"{self.username} ({self.role})"
