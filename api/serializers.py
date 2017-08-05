from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Semester, Course


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',)