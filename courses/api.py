from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from .models import Sector, Subject, Course

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

router = routers.DefaultRouter()
router.register(r"sectors", SectorViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
