# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 22:08
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import truncatechars, slugify


def gen_slug(apps, schema_editor):
    Astronauts = apps.get_model('api', 'Astronauts')
    for item in Astronauts.objects.all():
        item.slug = slugify('%s-%s' % (item.name, item.id))
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_astronauts_slug'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_slug, reverse_code=migrations.RunPython.noop),
    ]