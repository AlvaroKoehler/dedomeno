# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0035_auto_20161202_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AgencyLocationSource',
            new_name='AgencyLocalizationSource',
        ),
    ]
