# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0107_remove_property_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
