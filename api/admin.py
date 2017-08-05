from django.contrib import admin

# Register your models here.
from api.models import Semester, Course

admin.site.register(Semester)
admin.site.register(Course)