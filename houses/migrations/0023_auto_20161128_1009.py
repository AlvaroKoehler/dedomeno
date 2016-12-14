# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0022_auto_20161128_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='agency',
            field=models.ManyToManyField(blank=True, help_text='If blank there is not an agency involved', to='houses.Agency'),
        ),
        migrations.AlterField(
            model_name='house',
            name='source',
            field=models.ManyToManyField(blank=True, to='houses.Source'),
        ),
    ]
