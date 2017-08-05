from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models import Semester, Course
from api.serializers import SemesterSerializer, CourseSerializer, UserSerializer


class SemesterList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SemesterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Course.objects.all().order_by('-id')
        else:
            return Course.objects.filter(user=self.request.user).order_by('-id')

class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Course.objects.all()
        else:
            return Course.objects.filter(user=self.request.user)


class UserGetOrCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = None

        # if user is exists
        if self.request.user.is_anonymous and \
                        'username' in request.data:
            try:
                user = User.objects.get(
                    username=request.data.get('username'),
                )
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                pass

        # else if user is Authenticated with token
        elif not self.request.user.is_anonymous and self.request.user.username == request.data.get('username'):
            user = self.request.user

        # if user object exists, then return user data
        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return self.create(request, *args, **kwargs)
