# Generated by Django 5.0 on 2024-01-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_appointment_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='event_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
