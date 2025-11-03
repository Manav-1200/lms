from django.urls import path
from . import views

app_name = "dashboards"

urlpatterns = [
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    path("instructor/", views.instructor_dashboard, name="instructor_dashboard"),
    path("student/", views.student_dashboard, name="student_dashboard"),
    path("sponsor/", views.sponsor_dashboard, name="sponsor_dashboard"),
]
