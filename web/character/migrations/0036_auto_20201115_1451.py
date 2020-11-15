# Generated by Django 2.2.16 on 2020-11-15 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("character", "0035_auto_20191228_1417"),
    ]

    operations = [
        migrations.AddField(
            model_name="rosterentry",
            name="show_positions",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="PlayerPosition",
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
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "players",
                    models.ManyToManyField(
                        related_name="player_positions", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
