# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-23 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_auto_20191123_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'verbose_name': '学生作品', 'verbose_name_plural': '学生作品'},
        ),
        migrations.AlterModelTable(
            name='artwork',
            table='art',
        ),
    ]
