# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_auto_20160306_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='institute',
            field=models.CharField(max_length=120),
        ),
    ]