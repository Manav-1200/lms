from django.contrib.auth.models import AbstractUser
from django.db import models

# A custom user model with a role field so we can distinguish student/instructor/admin
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("admin", "Admin"),
        ("sponsor", "Sponsor"),
    ]
    # Role field with default to student for newly registered users
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    # Optional full name field; AbstractUser already has first_name/last_name
    full_name = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        # If this user is superuser this ensure role is admin
        if self.is_superuser:
            self.role = "admin"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
