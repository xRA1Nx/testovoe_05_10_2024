from __future__ import annotations
from gamification.logic.interactors.player import player__prize_title
from gamification.models import Prize


def prize__create() -> Prize:
    """ Создание объекта "Приз". """
    title = player__prize_title()
    return Prize.objects.create(title=title)
