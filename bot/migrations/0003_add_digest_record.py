# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_rename_last_daily'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDigestRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('messages', models.TextField(blank=True, max_length=1048, null=True)),
                ('count', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='notification',
            name='last_daily_digest_analysis',
        ),
    ]
