# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0026_pad_agency_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pad',
            name='agency_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
