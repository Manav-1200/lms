from django.urls import path
from . import views

app_name = "sponsors"

urlpatterns = [
    # simple placeholder; no elaborate payment integration here
    path("", views.sponsor_list, name="list"),
]
