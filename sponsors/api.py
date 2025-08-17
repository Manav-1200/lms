from django.urls import path, include
from rest_framework import routers, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sponsorship
from .serializers import SponsorshipSerializer

class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.select_related("sponsor", "student").all()
    serializer_class = SponsorshipSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["sponsor", "student"]
    search_fields = ["sponsor__username", "student__username"]
    ordering_fields = ["created_at", "amount"]

router = routers.DefaultRouter()
router.register(r"sponsorships", SponsorshipViewSet, basename="sponsorship")

urlpatterns = [
    path("", include(router.urls)),
]
