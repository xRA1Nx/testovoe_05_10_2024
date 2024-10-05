from __future__ import annotations
from common.dto import BaseDto


class PlayerLevelCSVRowReportDto(BaseDto):
    player_id: str
    level_title: str
    is_level_completed: bool
    prize_title: str
