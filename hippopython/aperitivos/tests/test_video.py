import pytest
from django.urls import reverse
from model_mommy import mommy

from hippopython.aperitivos.models import Video
from hippopython.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_existe(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existe',)))


def test_status_code_error(resp_video_nao_existe):
    assert resp_video_nao_existe.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}&amp;'
                          'badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"'
                    )
