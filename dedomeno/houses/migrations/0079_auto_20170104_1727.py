# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0078_auto_20170104_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]