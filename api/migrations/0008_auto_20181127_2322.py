# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-27 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_astronaut_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='astronauts',
            old_name='born',
            new_name='date_of_birth',
        ),
        migrations.AddField(
            model_name='astronauts',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='astronauts',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='astronauts',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]