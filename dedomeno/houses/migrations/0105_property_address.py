# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 19:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0104_property_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
