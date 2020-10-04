# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpdesk", "0009_auto_20170521_1705"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="participants",
        ),
        migrations.AlterField(
            model_name="customfield",
            name="label",
            field=models.CharField(
                help_text="The display label for this field",
                max_length=30,
                verbose_name="Label",
            ),
        ),
    ]
