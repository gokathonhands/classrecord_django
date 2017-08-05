from django.db import models

# Create your models here.

class Semester(models.Model):
    year = models.IntegerField(default=2017)
    season = models.CharField(max_length=100, default="spring")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('year', 'season',)

    def __str__(self):
        return self.year + self.season

class Course(models.Model):
    # user = models.ForeignKey('auth.User', default=1)
    semester_id = models.ForeignKey('api.Semester')
    name = models.CharField(max_length=100, default="공학수학")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name