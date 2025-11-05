from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import EnrollmentViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
