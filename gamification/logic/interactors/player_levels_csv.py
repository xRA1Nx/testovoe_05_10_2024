from __future__ import annotations

import csv
import io

from gamification.dto import PlayerLevelCSVRowReportDto


def player_levels__report_dtos_csv_to_bytes(
        *, dto_list: list[PlayerLevelCSVRowReportDto], batch_size: int = 1000
) -> bytes:
    """
    Формирует байтовое представление отчета csv по уровням игрока на основании заданного размера перечня строк.
    Размер перечня строк используется для генетатора, чтобы экономить память ОЗУ.
    """
    csv_buffer = io.BytesIO()
    writer = csv.writer(io.TextIOWrapper(csv_buffer, encoding='utf-8', newline=''))
    writer.writerow(["id игрока", "название уровня", "пройден ли уровень", "полученный приз за уровень"])
    for batch in players_level__csv_report_batches_generator(batch_size=batch_size, rows=dto_list):
        writer.writerows(batch)
    csv_buffer.seek(0)
    return csv_buffer.getvalue()


def players_level__csv_report_batches_generator(
        *, batch_size: int = 1000, rows: list[PlayerLevelCSVRowReportDto]
) -> list[tuple[str, str, str, str]]:
    """
    Функция генератор, с использованием итерации по батчам
    """
    rows_count = len(rows)
    for start in range(0, rows_count, batch_size):
        batch = players_level__batch_csv_rows(
            start=start, batch_size=batch_size, rows_count=rows_count, rows=rows
        )
        yield batch


def players_level__batch_csv_rows(
        *, start: int, batch_size: int, rows_count: int, rows: list[PlayerLevelCSVRowReportDto]
) -> list[tuple[str, str, str, str]]:
    """ Формирование списка строк в рамках батча."""

    end = min(start + batch_size, rows_count)
    batch_row_list = []
    for i in range(start, end):
        dto = rows[i]
        dto_representation = player_level__dto_to_csv_row_representation(dto=dto)
        batch_row_list.append(dto_representation)
    return batch_row_list


def player_level__dto_to_csv_row_representation(*, dto: PlayerLevelCSVRowReportDto) -> tuple[str, str, str, str]:
    """ Формирование текстовых данных каждой строке на основании dto. """
    return dto.player_id, dto.level_title, str(dto.is_level_completed), dto.prize_title
