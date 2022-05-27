from django.urls import path

from hippopython.aperitivos.views import video, indice

app_name = 'aperitivos'
urlpatterns = [
    path('', indice, name='indice'),
    path('<slug:slug>', video, name='video'),
]
