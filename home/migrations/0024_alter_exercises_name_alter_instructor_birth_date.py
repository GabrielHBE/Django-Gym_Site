# Generated by Django 5.1.5 on 2025-01-30 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_workout_current_workout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 30, 17, 59, 54, 168950)),
        ),
    ]
