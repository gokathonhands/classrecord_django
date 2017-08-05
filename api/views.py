from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Semester, Course
from api.serializers import SemesterSerializer, CourseSerializer


class SemesterList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SemesterDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class CourseList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer