from django.urls import path
from .views import sponsor_dashboard

app_name = "sponsors"

urlpatterns = [
    path("dashboard/", sponsor_dashboard, name="dashboard"),
]
