from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^semester/$', views.SemesterList.as_view()),
    url(r'^semester/(?P<pk>[0-9]+)$', views.SemesterDetail.as_view()),
]