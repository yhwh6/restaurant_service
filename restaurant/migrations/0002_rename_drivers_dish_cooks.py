# Generated by Django 4.1.7 on 2023-04-03 08:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dish",
            old_name="drivers",
            new_name="cooks",
        ),
    ]