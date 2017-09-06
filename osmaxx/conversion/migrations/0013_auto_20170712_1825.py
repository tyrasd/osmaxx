# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-12 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0012_auto_20170511_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametrization',
            name='out_srs',
            field=models.IntegerField(blank=True, choices=[('Global coordinate reference systems', ((4326, 'WGS 84'), (3857, 'Pseudo-Mercator'), (4322, 'WGS 72'), (4269, 'NAD 83'), (4277, 'OSGB 36'))), ('UTM zones', ((32601, 'UTM Zone 1, northern hemisphere'), (32602, 'UTM Zone 2, northern hemisphere'), (32603, 'UTM Zone 3, northern hemisphere'), (32604, 'UTM Zone 4, northern hemisphere'), (32605, 'UTM Zone 5, northern hemisphere'), (32606, 'UTM Zone 6, northern hemisphere'), (32607, 'UTM Zone 7, northern hemisphere'), (32608, 'UTM Zone 8, northern hemisphere'), (32609, 'UTM Zone 9, northern hemisphere'), (32610, 'UTM Zone 10, northern hemisphere'), (32611, 'UTM Zone 11, northern hemisphere'), (32612, 'UTM Zone 12, northern hemisphere'), (32613, 'UTM Zone 13, northern hemisphere'), (32614, 'UTM Zone 14, northern hemisphere'), (32615, 'UTM Zone 15, northern hemisphere'), (32616, 'UTM Zone 16, northern hemisphere'), (32617, 'UTM Zone 17, northern hemisphere'), (32618, 'UTM Zone 18, northern hemisphere'), (32619, 'UTM Zone 19, northern hemisphere'), (32620, 'UTM Zone 20, northern hemisphere'), (32621, 'UTM Zone 21, northern hemisphere'), (32622, 'UTM Zone 22, northern hemisphere'), (32623, 'UTM Zone 23, northern hemisphere'), (32624, 'UTM Zone 24, northern hemisphere'), (32625, 'UTM Zone 25, northern hemisphere'), (32626, 'UTM Zone 26, northern hemisphere'), (32627, 'UTM Zone 27, northern hemisphere'), (32628, 'UTM Zone 28, northern hemisphere'), (32629, 'UTM Zone 29, northern hemisphere'), (32630, 'UTM Zone 30, northern hemisphere'), (32631, 'UTM Zone 31, northern hemisphere'), (32632, 'UTM Zone 32, northern hemisphere'), (32633, 'UTM Zone 33, northern hemisphere'), (32634, 'UTM Zone 34, northern hemisphere'), (32635, 'UTM Zone 35, northern hemisphere'), (32636, 'UTM Zone 36, northern hemisphere'), (32637, 'UTM Zone 37, northern hemisphere'), (32638, 'UTM Zone 38, northern hemisphere'), (32639, 'UTM Zone 39, northern hemisphere'), (32640, 'UTM Zone 40, northern hemisphere'), (32641, 'UTM Zone 41, northern hemisphere'), (32642, 'UTM Zone 42, northern hemisphere'), (32643, 'UTM Zone 43, northern hemisphere'), (32644, 'UTM Zone 44, northern hemisphere'), (32645, 'UTM Zone 45, northern hemisphere'), (32646, 'UTM Zone 46, northern hemisphere'), (32647, 'UTM Zone 47, northern hemisphere'), (32648, 'UTM Zone 48, northern hemisphere'), (32649, 'UTM Zone 49, northern hemisphere'), (32650, 'UTM Zone 50, northern hemisphere'), (32651, 'UTM Zone 51, northern hemisphere'), (32652, 'UTM Zone 52, northern hemisphere'), (32653, 'UTM Zone 53, northern hemisphere'), (32654, 'UTM Zone 54, northern hemisphere'), (32655, 'UTM Zone 55, northern hemisphere'), (32656, 'UTM Zone 56, northern hemisphere'), (32657, 'UTM Zone 57, northern hemisphere'), (32658, 'UTM Zone 58, northern hemisphere'), (32659, 'UTM Zone 59, northern hemisphere'), (32660, 'UTM Zone 60, northern hemisphere'), (32701, 'UTM Zone 1, southern hemisphere'), (32702, 'UTM Zone 2, southern hemisphere'), (32703, 'UTM Zone 3, southern hemisphere'), (32704, 'UTM Zone 4, southern hemisphere'), (32705, 'UTM Zone 5, southern hemisphere'), (32706, 'UTM Zone 6, southern hemisphere'), (32707, 'UTM Zone 7, southern hemisphere'), (32708, 'UTM Zone 8, southern hemisphere'), (32709, 'UTM Zone 9, southern hemisphere'), (32710, 'UTM Zone 10, southern hemisphere'), (32711, 'UTM Zone 11, southern hemisphere'), (32712, 'UTM Zone 12, southern hemisphere'), (32713, 'UTM Zone 13, southern hemisphere'), (32714, 'UTM Zone 14, southern hemisphere'), (32715, 'UTM Zone 15, southern hemisphere'), (32716, 'UTM Zone 16, southern hemisphere'), (32717, 'UTM Zone 17, southern hemisphere'), (32718, 'UTM Zone 18, southern hemisphere'), (32719, 'UTM Zone 19, southern hemisphere'), (32720, 'UTM Zone 20, southern hemisphere'), (32721, 'UTM Zone 21, southern hemisphere'), (32722, 'UTM Zone 22, southern hemisphere'), (32723, 'UTM Zone 23, southern hemisphere'), (32724, 'UTM Zone 24, southern hemisphere'), (32725, 'UTM Zone 25, southern hemisphere'), (32726, 'UTM Zone 26, southern hemisphere'), (32727, 'UTM Zone 27, southern hemisphere'), (32728, 'UTM Zone 28, southern hemisphere'), (32729, 'UTM Zone 29, southern hemisphere'), (32730, 'UTM Zone 30, southern hemisphere'), (32731, 'UTM Zone 31, southern hemisphere'), (32732, 'UTM Zone 32, southern hemisphere'), (32733, 'UTM Zone 33, southern hemisphere'), (32734, 'UTM Zone 34, southern hemisphere'), (32735, 'UTM Zone 35, southern hemisphere'), (32736, 'UTM Zone 36, southern hemisphere'), (32737, 'UTM Zone 37, southern hemisphere'), (32738, 'UTM Zone 38, southern hemisphere'), (32739, 'UTM Zone 39, southern hemisphere'), (32740, 'UTM Zone 40, southern hemisphere'), (32741, 'UTM Zone 41, southern hemisphere'), (32742, 'UTM Zone 42, southern hemisphere'), (32743, 'UTM Zone 43, southern hemisphere'), (32744, 'UTM Zone 44, southern hemisphere'), (32745, 'UTM Zone 45, southern hemisphere'), (32746, 'UTM Zone 46, southern hemisphere'), (32747, 'UTM Zone 47, southern hemisphere'), (32748, 'UTM Zone 48, southern hemisphere'), (32749, 'UTM Zone 49, southern hemisphere'), (32750, 'UTM Zone 50, southern hemisphere'), (32751, 'UTM Zone 51, southern hemisphere'), (32752, 'UTM Zone 52, southern hemisphere'), (32753, 'UTM Zone 53, southern hemisphere'), (32754, 'UTM Zone 54, southern hemisphere'), (32755, 'UTM Zone 55, southern hemisphere'), (32756, 'UTM Zone 56, southern hemisphere'), (32757, 'UTM Zone 57, southern hemisphere'), (32758, 'UTM Zone 58, southern hemisphere'), (32759, 'UTM Zone 59, southern hemisphere'), (32760, 'UTM Zone 60, southern hemisphere')))], default=4326, help_text='EPSG code of the output spatial reference system', null=True, verbose_name='output SRS'),
        ),
    ]