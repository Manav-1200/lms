from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sponsorship

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ("sponsor", "student", "amount", "created_at")
    list_filter = ("sponsor",)
    search_fields = ("sponsor__username", "student__username")
