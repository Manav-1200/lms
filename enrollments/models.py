from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from courses.models import Course, Assessment

User = settings.AUTH_USER_MODEL

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("dropped", "Dropped"),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # 0 - 100
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} → {self.course} ({self.status})"


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="submissions")
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="submissions")
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("enrollment", "assessment")

    def __str__(self):
        return f"{self.enrollment.student} — {self.assessment.title} ({self.score})"
