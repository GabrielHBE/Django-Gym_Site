# Generated by Django 5.1.5 on 2025-01-22 01:26

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_userparams_user_alter_instructor_birth_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userparams',
            name='name',
        ),
        migrations.AddField(
            model_name='userparams',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_params', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 21, 22, 26, 15, 157376)),
        ),
        migrations.AlterField(
            model_name='userparams',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 21, 22, 26, 15, 157376)),
        ),
    ]
