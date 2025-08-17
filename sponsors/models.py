from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Sponsorship(models.Model):
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sponsorships")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sponsored_students")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sponsorships"

    def __str__(self):
        return f"{self.sponsor} → {self.student} ({self.amount})"
