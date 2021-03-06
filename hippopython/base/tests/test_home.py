import pytest
from django.urls import reverse

from hippopython.django_assertions import assert_contains


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_title(resposta):
    assert_contains(resposta, '<title>hippopython - home</title>')


def test_home_link(resposta):
    assert_contains(resposta, f'href="{reverse("base:home")}">hippopython</a>')


def test_email_link(resposta):
    assert_contains(resposta, f'href="mailto: michel4alves.python@gmail.com"')
