# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20170422_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsdetails',
            name='month',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='eventsdetails',
            name='year',
            field=models.IntegerField(default=2017),
        ),
    ]
