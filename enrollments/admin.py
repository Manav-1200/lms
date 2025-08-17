from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enrollment, Submission

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "status", "progress", "enrolled_at")
    list_filter = ("status", "course")
    search_fields = ("student__username", "course__title")

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "assessment", "score", "submitted_at")
    list_filter = ("assessment",)
    search_fields = ("enrollment__student__username", "assessment__title")
