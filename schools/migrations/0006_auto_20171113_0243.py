# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_major_school_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='school_id',
            new_name='school',
        ),
    ]
