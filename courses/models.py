from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    DIFFICULTY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_taught")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default="beginner")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assessments")
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    max_score = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.course.title} — {self.title}"
