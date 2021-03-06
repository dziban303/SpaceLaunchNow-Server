# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(blank=True)),
                ('netstamp', models.IntegerField(blank=True, null=True)),
                ('wsstamp', models.IntegerField(blank=True, null=True)),
                ('westamp', models.IntegerField(blank=True, null=True)),
                ('inhold', models.IntegerField(blank=True, null=True)),
                ('rocket_name', models.CharField(blank=True, default=b'', max_length=255)),
                ('mission_name', models.CharField(blank=True, default=b'', max_length=255)),
                ('location_name', models.CharField(blank=True, default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wasNotifiedTwentyFourHour', models.BooleanField(default=False)),
                ('wasNotifiedOneHour', models.BooleanField(default=False)),
                ('wasNotifiedTenMinutes', models.BooleanField(default=False)),
                ('wasNotifiedDailyDigest', models.BooleanField(default=False)),
                ('last_daily_digest_post', models.DateTimeField(blank=True, null=True)),
                ('last_twitter_post', models.DateTimeField(blank=True, null=True)),
                ('last_net_stamp', models.IntegerField(blank=True, null=True)),
                ('last_net_stamp_timestamp', models.DateTimeField(blank=True, null=True)),
                ('launch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bot.Launch')),
            ],
        ),
    ]
