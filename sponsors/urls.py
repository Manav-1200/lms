from django.urls import path
from . import views

app_name = "sponsors"

urlpatterns = [
    path("students/", views.SponsorStudentListView.as_view(), name="students"),
]
