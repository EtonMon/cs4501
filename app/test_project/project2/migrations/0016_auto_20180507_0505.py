# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-07 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0015_spark_entries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spark_entries',
            name='id',
        ),
        migrations.AlterField(
            model_name='spark_entries',
            name='item_id',
            field=models.CharField(default='DEFAULT_ITEM_ID', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spark_entries',
            name='recommended_items',
            field=models.TextField(),
        ),
    ]
