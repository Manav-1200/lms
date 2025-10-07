from django.contrib import admin
from .models import Sector, Subject, Course

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "sector")
    list_filter = ("sector",)
    search_fields = ("name",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "instructor", "duration_weeks", "created_at")
    list_filter = ("subject",)
    search_fields = ("title", "instructor__username")
