import pytest
from django.urls import reverse
from model_mommy import mommy

from hippopython.django_assertions import assert_contains
from hippopython.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client_com_usuario_logado, aula):
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{aula.vimeo_id}&amp;'
                          'badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"'
                    )


def test_breadcrumb(resp, modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">'
                          f'{modulo.titulo}</a></li>'
                    )


@pytest.fixture
def resp_sem_usuario(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def teste_usuario_nao_logado_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
