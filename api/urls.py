from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^users$', views.UserGetOrCreate.as_view(), name='user-get-or-create'),
    url(r'^semester/$', views.SemesterList.as_view()),
    url(r'^semester/(?P<pk>[0-9]+)$', views.SemesterDetail.as_view()),
    url(r'^course/$', views.CourseList.as_view()),
    url(r'^course/(?P<pk>[0-9]+)$', views.CourseDetail.as_view()),
]