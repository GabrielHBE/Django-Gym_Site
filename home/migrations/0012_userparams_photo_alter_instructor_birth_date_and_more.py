# Generated by Django 5.1.5 on 2025-01-22 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_userparams_user_alter_instructor_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userparams',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 9, 16, 19, 593649)),
        ),
        migrations.AlterField(
            model_name='userparams',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 9, 16, 19, 593649)),
        ),
    ]
