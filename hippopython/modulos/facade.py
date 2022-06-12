from typing import List

from hippopython.modulos.models import Modulo, Aula
from django.db.models.query import Prefetch

def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_do_modulo_ordenadas(modulo:Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug: str) -> Aula:
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    return list(Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
    ).all())
