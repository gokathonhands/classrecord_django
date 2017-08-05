from django.contrib import admin

# Register your models here.
from api.models import Semester, Course, MyCourse

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(MyCourse)