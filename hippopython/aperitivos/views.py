from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def video(request, slug):
    return render(request, 'aperitivos/video.html')
