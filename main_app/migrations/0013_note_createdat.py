# Generated by Django 3.2.9 on 2021-12-06 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20211206_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='createdAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
