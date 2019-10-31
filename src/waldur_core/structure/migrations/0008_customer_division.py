# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-20 13:03
from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0007_customer_blocked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.Division')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'division',
            },
        ),
        migrations.CreateModel(
            name='DivisionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'division type',
            },
        ),
        migrations.AddField(
            model_name='division',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.DivisionType'),
        ),
        migrations.AddField(
            model_name='customer',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.Division'),
        ),
    ]
