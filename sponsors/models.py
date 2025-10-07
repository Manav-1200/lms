from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class Sponsorship(models.Model):
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sponsorships")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sponsorships")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sponsorships"

    def __str__(self):
        return f"{self.sponsor.username} sponsored {self.course.title}"
