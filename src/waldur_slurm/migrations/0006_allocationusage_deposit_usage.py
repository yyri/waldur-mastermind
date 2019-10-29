# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-05 22:40
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_slurm', '0005_add_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocationusage',
            name='deposit_usage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
