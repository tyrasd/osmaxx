# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excerptexport', '0022_transfer_output_files_from_extraction_orders_to_exports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excerpt',
            old_name='bounding_geometry',
            new_name='bounding_geometry_old',
        ),
    ]
