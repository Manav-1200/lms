from django.db import models
from django.conf import settings
from courses.models import Course, Lesson  # Make sure Lesson exists in courses.models

class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateTimeField(auto_now_add=True)
    payment_completed = models.BooleanField(default=False)
    progress_percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"


class Submission(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="submissions")
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.lesson.title} submission"
