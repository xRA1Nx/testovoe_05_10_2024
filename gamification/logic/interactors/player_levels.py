from __future__ import annotations

from django.db.models import QuerySet

from gamification.dto import PlayerLevelCSVRowReportDto
from gamification.logic.selectors.player_levels import player_levels__with_related_fields_for_csv_reports
from gamification.models import PlayerLevel


def player_levels__report_dtos(
        *, player_levels: QuerySet[PlayerLevel] | None = None
) -> list[PlayerLevelCSVRowReportDto]:
    """
    Собирает все dto строки отчета по каждой из позиции Уровня Игрока в единый список.
    """
    dto_list = []
    player_levels_with_related_fields = player_levels__with_related_fields_for_csv_reports(qs=player_levels)
    for player_level in player_levels_with_related_fields:
        level_prize_dtos = player_level__report_dtos_by_level_prizes(player_level=player_level)
        dto_list.extend(level_prize_dtos)
    return dto_list


def player_level__report_dtos_by_level_prizes(*, player_level: PlayerLevel) -> list[PlayerLevelCSVRowReportDto]:
    """
    Логика формирования dto строки отчета в разрезе по призам за уровень для каждого уровня игрока.
    """
    player_level_dtos = []
    for level_prize in player_level.level.level_prizes.all():
        dto = PlayerLevelCSVRowReportDto(
            player_id=player_level.player.player_id,
            level_title=player_level.level.title,
            is_level_completed=player_level.is_completed,
            prize_title=level_prize.level.title,
        )
        player_level_dtos.append(dto)
    return player_level_dtos
