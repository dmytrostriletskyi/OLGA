# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph_creator', '0004_auto_20170316_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastorage',
            name='students_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
