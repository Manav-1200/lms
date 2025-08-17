from rest_framework import serializers
from .models import Enrollment, Submission

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["id", "student", "course", "status", "progress", "enrolled_at"]

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "enrollment", "assessment", "submitted_at", "score"]
