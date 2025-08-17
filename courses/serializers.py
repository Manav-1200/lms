from rest_framework import serializers
from .models import Course, Lesson, Assessment

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source="instructor.get_full_name", read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "instructor", "instructor_name", "difficulty", "is_active", "created_at"]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "course", "title", "content", "order"]

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["id", "course", "title", "due_date", "max_score"]
