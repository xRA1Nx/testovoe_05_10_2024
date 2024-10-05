from __future__ import annotations

import typing

from django.utils.timezone import localdate
from gamification.models import LevelPrize

if typing.TYPE_CHECKING:
    from gamification.models import Level, Prize


def level_prize__create(*, level: Level, prize: Prize) -> LevelPrize:
    """ Создание объекта "Приз за уровень" """
    return LevelPrize.objects.create(
        level=level,
        prize=prize,
        received=localdate()  # по хорошему это поле должно null=True и заполняться таской отдельно,
        # по факту вручения пользователя подарка.
    )
