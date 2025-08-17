from django.urls import path, include
from rest_framework import routers, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course, Lesson, Assessment
from .serializers import CourseSerializer, LessonSerializer, AssessmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related("instructor")
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["difficulty", "instructor", "is_active"]
    search_fields = ["title", "description", "instructor__username", "instructor__first_name", "instructor__last_name"]
    ordering_fields = ["created_at", "title"]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["course"]
    search_fields = ["title", "content"]

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["course"]
    search_fields = ["title"]

router = routers.DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"lessons", LessonViewSet, basename="lesson")
router.register(r"assessments", AssessmentViewSet, basename="assessment")

urlpatterns = [
    path("", include(router.urls)),
]
