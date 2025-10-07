from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Sector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="subjects")

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_taught")
    duration_weeks = models.PositiveIntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
