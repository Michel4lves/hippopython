from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Este site está em fase inicial de construção</body></html>')
