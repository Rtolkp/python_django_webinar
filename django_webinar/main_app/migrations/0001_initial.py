# Generated by Django 5.0.4 on 2024-04-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contactform",
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
                ("Name", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=254)),
                ("Subject", models.CharField(blank=True, max_length=100, null=True)),
                ("Message", models.TextField()),
            ],
        ),
    ]