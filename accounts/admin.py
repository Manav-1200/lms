from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add role to admin display and to some forms
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")
    # keep default UserAdmin fieldsets and add our role field
    fieldsets = UserAdmin.fieldsets + (("Extra fields", {"fields": ("role",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
