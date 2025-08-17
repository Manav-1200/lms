from django.apps import apps
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

GROUPS = ["Admin", "Instructor", "Student", "Sponsor"]

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Ensure groups exist after migrations for all apps
    if sender.label in {"accounts", "courses", "enrollments", "sponsors", "notifications", "dashboards"}:
        for name in GROUPS:
            Group.objects.get_or_create(name=name)
