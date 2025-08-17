from django.urls import path, include
from rest_framework import routers, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Enrollment, Submission
from .serializers import EnrollmentSerializer, SubmissionSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related("student", "course").all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "course", "student"]
    search_fields = ["student__username", "course__title"]
    ordering_fields = ["enrolled_at", "progress"]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.select_related("enrollment", "assessment").all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["assessment", "enrollment"]
    search_fields = ["assessment__title", "enrollment__student__username"]

router = routers.DefaultRouter()
router.register(r"enrollments", EnrollmentViewSet, basename="enrollment")
router.register(r"submissions", SubmissionViewSet, basename="submission")

urlpatterns = [
    path("", include(router.urls)),
]
