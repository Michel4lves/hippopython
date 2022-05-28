from django.shortcuts import render
from django.http import HttpResponse


videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '700105282?h=9948754776'},
    {'slug': 'instalacao-windows', 'titulo': 'Vídeo Instalação: Windows', 'vimeo_id': '714327563?h=3d4a20fea1'},
]


# videos = {
#     'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '700105282?h=9948754776'},
#     'instalacao-windows': {'titulo': 'Vídeo Instalação: Windows', 'vimeo_id': '714327563?h=3d4a20fea1'},
# }

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'video': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

# def video(request, slug):
#     video = videos[slug]
#     return render(request, 'aperitivos/video.html', context={'video': video})
