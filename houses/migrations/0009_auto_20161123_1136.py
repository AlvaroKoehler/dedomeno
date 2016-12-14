# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0008_auto_20161123_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='agency',
            field=models.ForeignKey(blank=True, help_text='If blank there is not an agency involved', null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.Agency'),
        ),
        migrations.AlterField(
            model_name='house',
            name='conditions',
            field=models.CharField(blank=True, choices=[('good', 'good'), ('bad', 'bad')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='equipment',
            field=models.ManyToManyField(blank=True, null=True, to='houses.Equipment'),
        ),
        migrations.AlterField(
            model_name='house',
            name='orientation',
            field=models.CharField(blank=True, choices=[('N', 'N'), ('NE', 'NE'), ('E', 'E'), ('S', 'S'), ('SW', 'SW'), ('W', 'W'), ('NW', 'NW')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner_phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
