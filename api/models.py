#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Semester(models.Model):
    year = models.IntegerField(default=2017)
    season = models.CharField(max_length=100, default="spring")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('year', 'season',)

    def __str__(self):
        return str(self.year) + str(self.season)

YEAR_CHOICES = (
    (17, 2017),
    (16, 2016),
)

TERM_CHOICES = (
    ("1R", "1R"),
    ("2R", "2R"),
)

DAY_CHOICES = (
    (0,"월"),
    (1,"화"),
    (2,"수"),
    (3,"목"),
    (4,"금"),
)

TIME_CHOICES = (
    (1, "1교시"),
    (2, "2교시"),
    (3, "3교시"),
    (4, "4교시"),
    (5, "5교시"),
    (6, "6교시"),
    (7, "7교시"),
    (8, "8교시"),
    (9, "9교시"),
)

class Course(models.Model):
    user = models.ForeignKey('auth.User', default=1)
    year = models.IntegerField(choices=YEAR_CHOICES, default=2017)
    term = models.CharField(choices=TERM_CHOICES, max_length=3, default="2R")
    courseCode = models.CharField(max_length=13, default="KECE109")
    courseName = models.CharField(max_length=30, default="공학수학")
    day = models.IntegerField(choices=DAY_CHOICES, default=0)
    startTime = models.IntegerField(choices=TIME_CHOICES, default=1)
    endTime = models.IntegerField(choices=TIME_CHOICES, default=1)
    buildingName = models.CharField(max_length=30, default="")
    roomType = models.CharField(max_length=30, default="")
    roomName = models.CharField(max_length=50, default="")
    profName = models.CharField(max_length=20, default="")
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('courseName',)

    def __str__(self):
        return self.courseName

# class MyCourse(models.Model):
#     semester = models.ForeignKey('api.Semester', default=1)
#     user_id = models.ForeignKey('auth.User', default=1)
#     course = models.ForeignKey('api.Course')
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('course__courseName',)
#
#     def __str__(self):
#         return self.course.courseName