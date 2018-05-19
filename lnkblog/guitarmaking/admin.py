from django.contrib import admin
from .models import Course, Schedule, Learning, Fee

# Register your models here.

admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Learning)
admin.site.register(Fee)