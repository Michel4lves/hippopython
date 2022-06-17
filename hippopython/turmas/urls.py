from django.urls import path

from hippopython.turmas import views

app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice'),
]
