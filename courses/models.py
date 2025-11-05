from django.db import models
from django.conf import settings

# Sector: e.g., IT, Hospitality, Arts
class Sector(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Subject: belongs to a sector (e.g., Data Science under IT)
class Subject(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="subjects")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Course: main entity students enroll in
class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=250)
    description = models.TextField()
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "instructor"}
    )
    duration_weeks = models.PositiveIntegerField(default=4)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Lesson: belongs to a course
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=250)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)  # order of lessons in the course
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

# Assessment: belongs to a lesson
class Assessment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="assessments")
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    total_marks = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson.title} - {self.title}"
