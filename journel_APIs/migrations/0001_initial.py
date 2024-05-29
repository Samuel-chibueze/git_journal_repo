# Generated by Django 5.0.2 on 2024-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
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
                ("bio", models.TextField(max_length=200)),
                ("phone_number", models.CharField(max_length=19)),
                ("approved", models.BooleanField(default=False)),
            ],
        ),
    ]
