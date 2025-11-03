from django.contrib import admin
from .models import Sector, Subject, Course

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "sector")
    search_fields = ("title", "sector__name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "instructor", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("subject",)
