from django.urls import path
from . import views

app_name = "dashboards"

urlpatterns = [
    path("admin/", views.AdminDashboardView.as_view(), name="admin"),
    path("sponsor/", views.SponsorDashboardView.as_view(), name="sponsor"),
]
