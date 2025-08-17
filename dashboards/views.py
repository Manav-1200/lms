from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import TemplateView
from accounts.models import User
from courses.models import Course
from enrollments.models import Enrollment
from sponsors.models import Sponsorship

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    """
    Admin dashboard: total users, active courses, enrollments.
    """
    template_name = "dashboards/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_users"] = User.objects.count()
        ctx["active_courses"] = Course.objects.filter(is_active=True).count()
        ctx["total_enrollments"] = Enrollment.objects.count()
        # Top 5 courses by enrollments
        ctx["top_courses"] = (
            Course.objects.annotate(n=Count("enrollments"))
            .order_by("-n")[:5]
            .values("title", "n")
        )
        return ctx


class SponsorDashboardView(LoginRequiredMixin, TemplateView):
    """
    Sponsor dashboard: sponsorship impact, student progress, fund utilization.
    """
    template_name = "dashboards/sponsor_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        sponsor = self.request.user
        sponsored = Sponsorship.objects.filter(sponsor=sponsor)
        ctx["total_funded"] = sum(s.amount for s in sponsored)
        student_ids = sponsored.values_list("student_id", flat=True)
        enrolls = Enrollment.objects.filter(student_id__in=student_ids)
        if enrolls.exists():
            ctx["avg_progress"] = round(sum(float(e.progress) for e in enrolls) / enrolls.count(), 2)
        else:
            ctx["avg_progress"] = 0.0
        ctx["students_count"] = len(set(student_ids))
        return ctx
