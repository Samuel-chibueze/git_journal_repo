# Generated by Django 5.0.2 on 2024-02-17 06:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("journel_APIs", "0002_rename_full_name_authors_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="publisher_model",
            old_name="full_name",
            new_name="name",
        ),
    ]
