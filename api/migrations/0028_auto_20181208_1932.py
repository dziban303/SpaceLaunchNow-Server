# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-08 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20181208_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='launch_library_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]