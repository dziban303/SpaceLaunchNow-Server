# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_auto_20180703_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='id',
            new_name='pad_id',
        ),
        migrations.AddField(
            model_name='location',
            name='agency_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='location_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
