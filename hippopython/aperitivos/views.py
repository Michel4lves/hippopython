from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '700105282?h=9948754776'},
        'instalacao-windows': {'titulo': 'Vídeo Instalação: Windows', 'vimeo_id': '714327563?h=3d4a20fea1'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
