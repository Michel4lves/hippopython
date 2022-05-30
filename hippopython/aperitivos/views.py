from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse



class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação', '700105282?h=9948754776'),
    Video('instalacao-windows', 'Vídeo Instalação: Windows', '714327563?h=3d4a20fea1'),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
