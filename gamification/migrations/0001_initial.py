# Generated by Django 5.1.1 on 2024-10-05 08:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('player_id', models.CharField(max_length=100)),
                ('current_boost_value', models.IntegerField(default=0, verbose_name='текущее значение буста')),
                ('activated_at', models.DateTimeField(blank=True, null=True, verbose_name='дата активации')),
                ('first_login_at', models.DateTimeField(blank=True, null=True, verbose_name='дата активации')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('change_value', models.SmallIntegerField(verbose_name='Величина на которую изменится значение текущего буста')),
                ('modification_type', models.CharField(choices=[('increment', 'Увеличение'), ('decrement', 'Уменьшение')], max_length=50, verbose_name='тип модификации буста')),
                ('boost_type', models.CharField(choices=[('manual', 'Ручное'), ('leveling', 'Прохождение уровн(я/eй)')], max_length=50, verbose_name='тип буста')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.player', verbose_name='Буст игрока')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.level')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.player')),
            ],
        ),
        migrations.CreateModel(
            name='LevelPrize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.DateField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.level')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.prize')),
            ],
        ),
    ]
