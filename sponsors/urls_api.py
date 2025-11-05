from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import SponsorshipViewSet

router = DefaultRouter()
router.register(r'sponsorships', SponsorshipViewSet, basename='sponsorship')

urlpatterns = [
    path('', include(router.urls)),
]
