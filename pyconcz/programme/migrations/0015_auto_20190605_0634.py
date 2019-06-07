# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-05 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0014_auto_20190529_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='free_tickets_count',
            field=models.PositiveSmallIntegerField(default=0, help_text='Count of free tickets (from API)'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='is_sold_out',
            field=models.BooleanField(default=False, verbose_name='Sold out'),
        ),
    ]
