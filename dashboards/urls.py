from django.urls import path
from . import views

app_name = "dashboards"

urlpatterns = [
    path("student/", views.student_dashboard, name="student"),
    path("instructor/", views.instructor_dashboard, name="instructor"),
    path("sponsor/", views.sponsor_dashboard, name="sponsor"),
    path("admin/", views.admin_dashboard, name="admin"),
]
