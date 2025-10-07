from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.sponsor_dashboard, name="sponsor_dashboard"),
]
