from __future__ import annotations

from django.db.models import QuerySet

from gamification.models import PlayerLevel


def player_levels__all() -> QuerySet[PlayerLevel]:
    return PlayerLevel.objects.all()


def player_levels__with_related_fields_for_csv_reports(
        qs: QuerySet[PlayerLevel] | None = None
) -> QuerySet[PlayerLevel]:
    if qs is None:
        qs = player_levels__all()

    return qs.select_related('level', 'player').prefetch_related('level__level_prizes__prize')
