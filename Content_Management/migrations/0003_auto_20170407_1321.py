# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-07 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Content_Management', '0002_auto_20170407_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='caandidate_status',
            new_name='candidate_status',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='consultancy_id',
            new_name='consultancy',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='questions',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candiate_interview_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]