from django.db import models
from django.conf import settings
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateTimeField(auto_now_add=True)
    payment_completed = models.BooleanField(default=False)
    progress_percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
