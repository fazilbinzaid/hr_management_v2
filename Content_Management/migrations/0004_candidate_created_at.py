# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-07 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Content_Management', '0003_auto_20170407_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
