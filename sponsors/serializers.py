from rest_framework import serializers
from .models import Sponsorship

class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ["id", "sponsor", "student", "amount", "note", "created_at"]
