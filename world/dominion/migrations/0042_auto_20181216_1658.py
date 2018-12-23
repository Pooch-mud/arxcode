# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-16 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0041_prestigenomination'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestigenomination',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prestigenomination',
            name='denied_by',
            field=models.ManyToManyField(related_name='_prestigenomination_denied_by_+', to='dominion.PlayerOrNpc'),
        ),
    ]