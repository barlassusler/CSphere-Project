# Generated by Django 4.2.8 on 2024-01-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventapplication",
            name="event_duration",
            field=models.TextField(),
        ),
    ]