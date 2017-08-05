from rest_framework import serializers

from api.models import Semester, Course, MyCourse


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = (
            '__all__'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            '__all__'
        )

class MyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = (
            'course',
            'semester',
        )