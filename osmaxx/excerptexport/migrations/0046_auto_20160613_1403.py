# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excerptexport', '0045_extractionorder_detail_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractionorder',
            name='detail_level',
            field=models.IntegerField(choices=[(120, 'Full Detail'), (60, 'Simplified')], default=120, verbose_name='detail level'),
        ),
    ]
