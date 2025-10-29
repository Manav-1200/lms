from django.db import models
from django.conf import settings

# Sector groups multiple subjects (IT, Arts, Hospitality etc).
class Sector(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Subject is under a sector (e.g., Data Science under IT)
class Subject(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="subjects")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"

# Courses are the main objects that students enroll in
class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=250)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={"role": "teacher"})
    created_at = models.DateTimeField(auto_now_add=True)
    duration_weeks = models.PositiveIntegerField(default=4)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title

# Assignments per course
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"

# Submissions by students for assignments
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={"role": "student"})
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} submission for {self.assignment.title}"
