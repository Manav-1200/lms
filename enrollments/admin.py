from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "date_enrolled", "payment_completed", "progress_percent")
    list_filter = ("payment_completed",)
    search_fields = ("student__username", "course__title")
