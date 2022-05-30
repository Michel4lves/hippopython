import pytest
from django.urls import reverse

from hippopython.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice',))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Vídeo Aperitivo: Motivação',
        'Vídeo Instalação: Windows'
    ]
)
def test_titulos_videos(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_link_videos(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
