# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0048_auto_20161226_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='house',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='house',
            name='is_online',
        ),
        migrations.RemoveField(
            model_name='house',
            name='offline_date',
        ),
        migrations.RemoveField(
            model_name='house',
            name='online_date',
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='is_completed',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='is_online',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='offline_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='online_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]