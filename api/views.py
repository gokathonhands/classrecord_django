from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Semester, Course, MyCourse
from api.serializers import SemesterSerializer, CourseSerializer, MyCourseSerializer


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

class MyCourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = MyCourseSerializer

    # def get_queryset(self):
    #     if self.request.user.is_anonymous:
    #         return MyCourse.objects.all().order_by('-id')
    #     else:
    #         return MyCourse.objects.filter(user=self.request.user).order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     return

class MyCourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = MyCourseSerializer

