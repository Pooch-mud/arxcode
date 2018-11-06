# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0004_auto_20181105_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shardhavenlayoutsquare',
            name='exit_east',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_west', to='exploration.ShardhavenLayoutExit'),
        ),
        migrations.AlterField(
            model_name='shardhavenlayoutsquare',
            name='exit_north',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_south', to='exploration.ShardhavenLayoutExit'),
        ),
        migrations.AlterField(
            model_name='shardhavenlayoutsquare',
            name='exit_south',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_north', to='exploration.ShardhavenLayoutExit'),
        ),
        migrations.AlterField(
            model_name='shardhavenlayoutsquare',
            name='exit_west',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_east', to='exploration.ShardhavenLayoutExit'),
        ),
    ]
