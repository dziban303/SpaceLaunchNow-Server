# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0019_auto_20180705_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='pad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Pad'),
        ),
    ]
