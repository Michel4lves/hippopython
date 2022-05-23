import pytest
from django.test import Client
from django.urls import reverse

from hippopython.django_assertions import assert_contains


@pytest.fixture
def resposta(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_title(resposta):
    assert_contains(resposta, '<title>hippopython - Curso Django</title>')


def test_home_link(resposta):
    assert_contains(resposta, f'href="{reverse("base:home")}">hippopython</a>')
