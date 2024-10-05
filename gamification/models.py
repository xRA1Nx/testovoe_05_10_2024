from django.db import models

from common.models import DefaultModel
from gamification.enums import BoostModificationTypeChoices, BoostTypeChoices


class Player(DefaultModel):
    """ Модель игрока """
    player_id = models.CharField(  # поля из задания, смущает что оно не уникально и дублирует по сути id
        max_length=100
    )
    current_boost_value = models.IntegerField(
        verbose_name='текущее значение буста', default=0
    )
    activated_at = models.DateTimeField(
        verbose_name='дата активации', null=True, blank=True
    )  # логика активации в зависимости от FLOW может являться датой первого входа
    first_login_at = models.DateTimeField(
        verbose_name='дата активации', null=True, blank=True
    )  # альтернативный вариант на случай если логика активации учетной записи не подразумевает "первого входа"


class Boost(DefaultModel):
    """ Модель бустов игрока """

    change_value = models.SmallIntegerField(
        verbose_name='Величина на которую изменится значение текущего буста'
    )
    modification_type = models.CharField(
        verbose_name='тип модификации буста', max_length=50, choices=BoostModificationTypeChoices.choices,
    )
    boost_type = models.CharField(
        verbose_name='тип буста', max_length=50, choices=BoostTypeChoices.choices,
    )

    player = models.ForeignKey(
        to="Player", verbose_name='Буст игрока', on_delete=models.CASCADE
    )


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField(max_length=255)


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed_at = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='level_prizes')
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
