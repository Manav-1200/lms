from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, InstructorProfile, StudentProfile, SponsorProfile

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username", "user__email")

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "user__email")

@admin.register(SponsorProfile)
class SponsorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization")
    search_fields = ("user__username", "user__email", "organization")
