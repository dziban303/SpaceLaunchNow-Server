# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-01 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20180502_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launcher',
            name='capability',
            field=models.CharField(blank=True, default='', max_length=2048),
        ),
    ]