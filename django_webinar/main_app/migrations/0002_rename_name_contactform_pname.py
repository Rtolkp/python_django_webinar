# Generated by Django 5.0.4 on 2024-04-17 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactform",
            old_name="Name",
            new_name="Pname",
        ),
    ]
