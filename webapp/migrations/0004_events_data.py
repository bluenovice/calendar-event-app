# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170422_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('date_begin', models.CharField(max_length=50)),
                ('date_end', models.CharField(max_length=50)),
                ('time_start', models.IntegerField()),
                ('time_ends', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]
