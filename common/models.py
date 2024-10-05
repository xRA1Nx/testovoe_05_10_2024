import uuid as uuid
from django.db import models


class Timestamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='изменен', editable=False, auto_now=True)


class DefaultModel(Timestamped):
    """Абстрактный класс для моделей."""

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
