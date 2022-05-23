from django.urls import path

from hippopython.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]