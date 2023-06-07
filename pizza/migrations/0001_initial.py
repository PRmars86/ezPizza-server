# Generated by Django 4.2.1 on 2023-06-07 00:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("description", models.CharField(max_length=500)),
                (
                    "toppings",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200), size=None
                    ),
                ),
                ("image", models.URLField()),
                ("price", models.FloatField()),
            ],
            options={"ordering": ["name"], },
        ),
    ]
