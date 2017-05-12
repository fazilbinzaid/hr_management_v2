# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-07 05:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('Admin_Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('consultancy_name', models.CharField(max_length=300, null=True)),
                ('website', models.CharField(max_length=300, null=True)),
                ('phone_no', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='admin_name',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
