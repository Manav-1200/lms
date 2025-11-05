from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import CourseViewSet, LessonViewSet, AssessmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'assessments', AssessmentViewSet, basename='assessment')

urlpatterns = [
    path('', include(router.urls)),
]
