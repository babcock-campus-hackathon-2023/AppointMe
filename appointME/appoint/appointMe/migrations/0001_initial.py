# Generated by Django 4.1.7 on 2023-03-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("email", models.CharField(blank=True, max_length=30, null=True)),
                ("password", models.CharField(max_length=30)),
                ("phone_no", models.CharField(max_length=35)),
            ],
        ),
    ]