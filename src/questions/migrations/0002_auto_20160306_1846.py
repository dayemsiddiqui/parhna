# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer', models.TextField(blank=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
