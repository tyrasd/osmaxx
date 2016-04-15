# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excerptexport', '0017_auto_20160310_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_format', models.TextField(choices=[('fgdb', 'ESRI File Geodatabase'), ('shapefile', 'ESRI Shapefile'), ('gpkg', 'GeoPackage'), ('spatialite', 'SpatiaLite'), ('garmin', 'Garmin navigation & map data')])),
                ('extraction_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exports', to='excerptexport.ExtractionOrder', verbose_name='extraction order')),
            ],
        ),
    ]
