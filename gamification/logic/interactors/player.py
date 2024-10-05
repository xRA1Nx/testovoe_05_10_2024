from __future__ import annotations

import typing

from common.exception import BusinessLogicException

if typing.TYPE_CHECKING:
    from gamification.models import PlayerLevel


def player__prize_title() -> str:
    return 'Логика генерации заголовка приза не описана в ТЗ, поэтому оставлю тут рандомных текст ))'


def player__validate_on_level_prize_creation(*, player_level: PlayerLevel):
    if not player_level.is_completed:
        raise BusinessLogicException("Начисление приза не возможно до момента завершения уровня")
