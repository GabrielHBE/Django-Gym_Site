# Generated by Django 5.1.5 on 2025-01-30 21:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_exercises_name_alter_instructor_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='home.workout'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 30, 18, 4, 40, 71231)),
        ),
    ]
