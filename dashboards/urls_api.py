from django.urls import path
from .views_api import DashboardSummaryAPI

urlpatterns = [
    path('summary/', DashboardSummaryAPI.as_view(), name='dashboard-summary'),
]
