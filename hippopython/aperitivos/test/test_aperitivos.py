import pytest
from django.urls import reverse

from hippopython.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="card-header">Vídeo Aperitivo: Motivação</h1>')


def test_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/700105282?h=9948754776&amp;'
                          'badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"'
                    )
