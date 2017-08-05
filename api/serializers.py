from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Semester, Course, Record


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = (
            '__all__'
        )

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'token',)

    def get_token(self, obj):
        token, crated = Token.objects.get_or_create(user=obj)
        return token.key

class CourseSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = (
            'year', 'term',
            'courseCode', 'courseName', 'day',
            'startTime', 'endTime', 'buildingName',
            'roomType', 'roomName', 'profName',
            'created',
        )

class RecordSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Record
        fields = (
            '__all__'
        )