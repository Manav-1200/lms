from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Lesson, Assessment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "difficulty", "is_active", "created_at")
    list_filter = ("difficulty", "is_active")
    search_fields = ("title", "description", "instructor__username", "instructor__email")

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "order")
    list_filter = ("course",)
    search_fields = ("title", "course__title")

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "due_date", "max_score")
    list_filter = ("course",)
    search_fields = ("title", "course__title")
