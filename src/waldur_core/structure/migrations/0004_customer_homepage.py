# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 09:50
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_order_by_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='homepage',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
