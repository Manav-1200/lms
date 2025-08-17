from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.db.models import Q
from enrollments.models import Enrollment
from .models import Sponsorship

class SponsorStudentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    Sponsors can filter students by status or progress.
    """
    template_name = "sponsors/sponsor_students.html"
    context_object_name = "enrollments"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Sponsor").exists()

    def get_queryset(self):
        student_ids = Sponsorship.objects.filter(sponsor=self.request.user).values_list("student_id", flat=True)
        qs = Enrollment.objects.select_related("student", "course").filter(student_id__in=student_ids)
        status = self.request.GET.get("status", "").strip()
        min_progress = self.request.GET.get("min_progress", "").strip()
        if status:
            qs = qs.filter(status=status)
        if min_progress:
            try:
                mp = float(min_progress)
                qs = qs.filter(progress__gte=mp)
            except ValueError:
                pass
        return qs
