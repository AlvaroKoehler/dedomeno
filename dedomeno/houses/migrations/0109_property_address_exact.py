# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0108_auto_20170320_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address_exact',
            field=models.NullBooleanField(),
        ),
    ]
