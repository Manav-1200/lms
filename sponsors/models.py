from django.db import models
from django.conf import settings
from courses.models import Course

class Sponsorship(models.Model):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sponsorships")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sponsorships")
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sponsorship"
        verbose_name_plural = "Sponsorships"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sponsor.username} sponsored {self.course.title} (${self.amount})"
