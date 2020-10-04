# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-17 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dominion", "0026_rpevent_risk"),
        ("objects", "0009_remove_objectdb_db_player"),
    ]

    operations = [
        migrations.CreateModel(
            name="FashionSnapshot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_date_created", models.DateTimeField(auto_now_add=True)),
                ("fame", models.IntegerField(blank=True, default=0)),
                (
                    "designer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="designer_snapshots",
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "fashion_item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fashion_snapshots",
                        to="objects.ObjectDB",
                    ),
                ),
                (
                    "fashion_model",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fashion_snapshots",
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fashion_snapshots",
                        to="dominion.Organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
