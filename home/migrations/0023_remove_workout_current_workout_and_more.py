# Generated by Django 5.1.5 on 2025-01-30 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_instructor_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='current_workout',
        ),
        migrations.AddField(
            model_name='userparams',
            name='current_workout',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 30, 11, 21, 7, 463206)),
        ),
    ]
