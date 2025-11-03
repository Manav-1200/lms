from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.sector_list, name="sector_list"),
    path("list/", views.course_list, name="course_list"),
    path("<int:pk>/", views.course_detail, name="course_detail"),
]
