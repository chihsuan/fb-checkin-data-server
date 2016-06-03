# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(db_index=True, max_length=16),
        ),
    ]
