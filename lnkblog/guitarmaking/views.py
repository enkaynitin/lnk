from django.shortcuts import render
from .models import Course, Schedule
# Create your views here.


def guitarmaking(request):
    courses = Course.objects.all()
    schedules = Schedule.objects.all()

    return render(
        request,
        'guitarmaking.html', {
            'courses': courses,
            'schedules': schedules,
        }
    )
