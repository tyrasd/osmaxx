# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0003_auto_20160528_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametrization',
            name='detail_level',
            field=models.IntegerField(choices=[(120, 'Complete'), (60, 'Simplified')], default=120, verbose_name='detail level'),
        ),
    ]
