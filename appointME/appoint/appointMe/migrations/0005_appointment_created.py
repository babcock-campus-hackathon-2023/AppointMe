# Generated by Django 4.1.7 on 2023-03-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointMe", "0004_rename_access_codes_appointment_access_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="created",
            field=models.DateTimeField(auto_now=True),
        ),
    ]