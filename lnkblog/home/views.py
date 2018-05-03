from django.shortcuts import render

# Create your views here.


def index(request, webview=False):

    return render(
        request,
        'home/index.html', {
        }
    )

