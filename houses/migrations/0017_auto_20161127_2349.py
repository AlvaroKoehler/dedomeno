# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0016_auto_20161127_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SourceHouseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type_transaction_name', models.CharField(blank=True, max_length=200, null=True)),
                ('house_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.HouseType')),
            ],
        ),
        migrations.CreateModel(
            name='SourceObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type_transaction_name', models.CharField(blank=True, max_length=100, null=True)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.ObjectType')),
            ],
        ),
        migrations.CreateModel(
            name='SourceTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_transaction_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='URLSourceTerritory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_source_territory_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='barrio',
            name='municipio_area',
        ),
        migrations.RemoveField(
            model_name='comunidadautonoma',
            name='country',
        ),
        migrations.RemoveField(
            model_name='municipioarea',
            name='zona',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='comunidad_autonoma',
        ),
        migrations.RemoveField(
            model_name='zona',
            name='provincia',
        ),
        migrations.RenameField(
            model_name='agency',
            old_name='name',
            new_name='agency_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='country_name',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='name',
            new_name='equipment_name',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='name',
            new_name='source_name',
        ),
        migrations.RenameField(
            model_name='territorialentity',
            old_name='name',
            new_name='territorial_entity_name',
        ),
        migrations.RemoveField(
            model_name='agencylocalization',
            name='barrio',
        ),
        migrations.RemoveField(
            model_name='house',
            name='barrio',
        ),
        migrations.RemoveField(
            model_name='source',
            name='attic_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='chalet_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='comercial_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='duplex_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='flat_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='holliday_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='house_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='land_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='new_construction_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='office_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='parking_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='rent_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='rustic_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='sale_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='share_url',
        ),
        migrations.RemoveField(
            model_name='territorialentity',
            name='depth_name',
        ),
        migrations.AddField(
            model_name='agencylocalization',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.TerritorialEntity'),
        ),
        migrations.AddField(
            model_name='house',
            name='territorial_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.TerritorialEntity'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='agency_localization',
            field=models.ManyToManyField(blank=True, through='houses.AgencyLocalization', to='houses.TerritorialEntity'),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.HouseType'),
        ),
        migrations.AlterField(
            model_name='house',
            name='object_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.ObjectType'),
        ),
        migrations.AlterField(
            model_name='house',
            name='transaction_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_transition_house', to='houses.Source'),
        ),
        migrations.DeleteModel(
            name='Barrio',
        ),
        migrations.DeleteModel(
            name='ComunidadAutonoma',
        ),
        migrations.DeleteModel(
            name='MunicipioArea',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
        migrations.DeleteModel(
            name='Zona',
        ),
        migrations.AddField(
            model_name='urlsourceterritory',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Source'),
        ),
        migrations.AddField(
            model_name='urlsourceterritory',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.TerritorialEntity'),
        ),
        migrations.AddField(
            model_name='sourcetransaction',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Source'),
        ),
        migrations.AddField(
            model_name='sourcetransaction',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Transaction'),
        ),
        migrations.AddField(
            model_name='sourceobjecttype',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Source'),
        ),
        migrations.AddField(
            model_name='sourcehousetype',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Source'),
        ),
        migrations.AddField(
            model_name='source',
            name='house_type_url',
            field=models.ManyToManyField(blank=True, null=True, through='houses.SourceHouseType', to='houses.HouseType'),
        ),
        migrations.AddField(
            model_name='source',
            name='object_type_url',
            field=models.ManyToManyField(blank=True, null=True, through='houses.SourceObjectType', to='houses.ObjectType'),
        ),
        migrations.AddField(
            model_name='source',
            name='territorial_url',
            field=models.ManyToManyField(blank=True, null=True, through='houses.URLSourceTerritory', to='houses.TerritorialEntity'),
        ),
        migrations.AddField(
            model_name='source',
            name='transaction_url',
            field=models.ManyToManyField(blank=True, null=True, through='houses.SourceTransaction', to='houses.Transaction'),
        ),
    ]
