from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "date_enrolled")
    list_filter = ("course",)
    search_fields = ("student__username", "course__title")
