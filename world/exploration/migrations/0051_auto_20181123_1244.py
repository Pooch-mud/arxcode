# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exploration", "0050_auto_20181123_1233"),
    ]

    operations = [
        migrations.AddField(
            model_name="shardhavenobstacle",
            name="peekable_closed",
            field=models.BooleanField(
                default=False,
                help_text=b"Can people see through this exit before it's been passed?",
            ),
        ),
        migrations.AddField(
            model_name="shardhavenobstacle",
            name="peekable_open",
            field=models.BooleanField(
                default=True,
                help_text=b"Can people see through this exit when it's been passed?",
            ),
        ),
    ]
