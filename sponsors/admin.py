from django.contrib import admin
from .models import Sponsorship

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ("sponsor", "course", "amount", "date")
    list_filter = ("course",)
    search_fields = ("sponsor__username", "course__title")
