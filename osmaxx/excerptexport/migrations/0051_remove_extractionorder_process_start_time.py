# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 07:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excerptexport', '0050_remove_extractionorder_download_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extractionorder',
            name='process_start_time',
        ),
    ]
