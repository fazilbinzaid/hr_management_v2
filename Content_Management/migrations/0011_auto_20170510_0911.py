# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-10 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content_Management', '0010_requirements_requirement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='requirement_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='requirement_name',
            field=models.CharField(max_length=50),
        ),
    ]
