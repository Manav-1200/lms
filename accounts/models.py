from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Extensible custom user.
    Roles are handled via Django Groups: Admin, Instructor, Student, Sponsor.
    """
    # Add extensible fields later if needed (phone, etc.)
    pass


class InstructorProfile(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="instructor_profile")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Instructor: {self.user.get_full_name() or self.user.username}"


class StudentProfile(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("inactive", "Inactive"),
    ]
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="student_profile")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return f"Student: {self.user.get_full_name() or self.user.username}"


class SponsorProfile(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="sponsor_profile")
    organization = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Sponsor: {self.user.get_full_name() or self.user.username}"
