from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
