# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import osmaxx.excerptexport.models.output_file


class Migration(migrations.Migration):

    dependencies = [
        ('excerptexport', '0034_auto_20160519_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outputfile',
            old_name='file',
            new_name='file_old',
        ),
        migrations.AddField(
            model_name='outputfile',
            name='file',
            field=models.FileField(blank=True, null=True,
                                   upload_to=osmaxx.excerptexport.models.output_file.uuid_directory_path,
                                   verbose_name='file', max_length=250),
        ),
    ]
