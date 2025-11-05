from rest_framework import viewsets
from .models import Sponsorship
from .serializers import SponsorshipSerializer

class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
