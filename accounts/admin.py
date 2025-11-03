from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")
    # add role to fieldsets so admin can set role
    fieldsets = UserAdmin.fieldsets + (
        ("Role & extra", {"fields": ("role", "full_name")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
