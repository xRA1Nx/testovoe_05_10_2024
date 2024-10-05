from __future__ import annotations

from django.db import transaction

from gamification.logic.facades.level_prize import level_prize__create
from gamification.logic.facades.prize import prize__create
from gamification.logic.interactors.player import player__validate_on_level_prize_creation
from gamification.models import PlayerLevel, LevelPrize


@transaction.atomic()
def player__prize_on_level_complete(*, player_level: PlayerLevel) -> LevelPrize:
    """ Присвоение игроку приза за прохождение уровня. """
    player__validate_on_level_prize_creation(player_level=player_level)
    prize = prize__create()
    return level_prize__create(level=player_level.level, prize=prize)
