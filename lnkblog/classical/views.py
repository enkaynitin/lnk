from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Guitar

# Create your views here.


def index(request):
    classical_guitars = Guitar.objects.all()

    return render(
        request,
        'classical-guitars.html', {
            'classical_guitars': classical_guitars,
            #'guitar_image': guitar_image
        }
    )