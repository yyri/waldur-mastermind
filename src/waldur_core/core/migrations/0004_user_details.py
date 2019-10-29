# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-22 10:01
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_enlarge_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra details from authentication backend.'),
        ),
    ]
