from __future__ import annotations

from django.db.models import QuerySet

from gamification.logic.interactors.player_levels import player_levels__report_dtos
from gamification.logic.interactors.player_levels_csv import player_levels__report_dtos_csv_to_bytes
from gamification.models import PlayerLevel


def player_levels__csv_report_in_bytes(*, player_levels: QuerySet[PlayerLevel] | None = None) -> bytes:
    """
    Получение байтового представления отчета в формате csv по Уровням игрока и вознаграждений за их прохождения.
    """
    dto_list = player_levels__report_dtos(player_levels=player_levels)
    return player_levels__report_dtos_csv_to_bytes(dto_list=dto_list)
