# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-27 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fashion", "0002_auto_20180826_0309"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fashionoutfit",
            name="name",
            field=models.CharField(db_index=True, max_length=80),
        ),
    ]
