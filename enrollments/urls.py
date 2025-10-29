from django.urls import path
from . import views

app_name = "enrollments"

urlpatterns = [
    path("enroll/<int:course_pk>/", views.enroll_in_course, name="enroll"),
]
