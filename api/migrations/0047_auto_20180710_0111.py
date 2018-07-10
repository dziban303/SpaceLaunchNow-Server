# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-10 05:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20180709_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='launcher',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 10, 1, 11, 29, 380000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launcher',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]