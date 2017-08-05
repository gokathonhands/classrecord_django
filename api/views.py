from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Semester
from api.serializers import SemesterSerializer


class SemesterList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SemesterDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer