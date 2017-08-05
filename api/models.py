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