from django.contrib import admin
from .models import Sector, Subject, Course, Assignment, Submission

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "sector")
    search_fields = ("title",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "instructor", "price", "created_at")
    list_filter = ("subject",)
    search_fields = ("title", "description")

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "due_date", "created_at")
    list_filter = ("course",)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("assignment", "student", "submitted_at", "grade")
    search_fields = ("student__username", "assignment__title")
