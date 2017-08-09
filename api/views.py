import json

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models import Semester, Course, Record
from api.serializers import SemesterSerializer, CourseSerializer, UserSerializer, RecordSerializer


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

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )

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

class RecordListCreate(ListCreateAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Record.objects.all().order_by('-id')
        else:
            return Record.objects.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer, course, filename):
        serializer.save(
            user=self.request.user,
            filename=filename,
            course=course
        )

    def post(self, request, *args, **kwargs):
        if 'voice' in request.FILES:
            request.data['file'] = request.FILES['voice']

        course = Course.objects.all().get(id=request.data['courseId'])
        filename = request.data['filename']

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer, course=course,
                                         filename=filename)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RecordRetrieveDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

@api_view(['GET', ])
def initialize_course(request):
    if request.user.is_anonymous():
        return Response({"message": "Bad Request, check Authorization Token"}, status=status.HTTP_401_UNAUTHORIZED)

    portal_account_fieldname = 'portalaccount'
    portal_pw_fieldname = 'password'
    if not portal_account_fieldname in request.GET or \
        not portal_pw_fieldname in request.GET:
        return Response({"message": "Bad Request, check querys"}, status=status.HTTP_400_BAD_REQUEST)

    portal_account = request.GET[portal_account_fieldname]
    portal_pw = request.GET[portal_pw_fieldname]

    import requests
    querys = {"client_id": "ku_it_fellow_student_app",
              "username": portal_account,
              "password": portal_pw,
              "grant_type": "password"
              }
    url = "https://openapi.korea.ac.kr/oauth/token"
    r = requests.get(url, params=querys, timeout=1)
    if r.status_code != 200:
        return Response({"message": "Wrong account, password"}, status=status.HTTP_400_BAD_REQUEST)

    access_token = r.json()['access_token']

    url = "https://openapi.korea.ac.kr/api/timetable"
    querys = {"format": "json",
              "year": 2017,
              "term": "2R",
              "access_token": access_token
              }

    r = requests.get(url, params=querys, timeout=1)
    jsonresponse = r.json()
    if r.status_code != 200:
        return Response({"message": "Unknown error"}, status=status.HTTP_400_BAD_REQUEST)


    if 'response' in jsonresponse:
        temp = jsonresponse['response']
        if 'data' in temp:
            courses = temp['data']
            for course in courses:
                serializer = CourseSerializer()
                course['user'] = request.user
                serializer.create(validated_data=course)

    view = CourseList.as_view()

    return view(request)