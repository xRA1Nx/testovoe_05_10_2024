from django.db.models import TextChoices


class BoostModificationTypeChoices(TextChoices):
    INCREMENT = 'increment', 'Увеличение'
    DECREMENT = 'decrement', 'Уменьшение'


class BoostTypeChoices(TextChoices):
    MANUAL = 'manual', 'Ручное'
    LEVELING = 'leveling', 'Прохождение уровн(я/eй)'
