# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170624_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayer_point',
            name='description',
            field=models.CharField(default='no_desc', max_length=512),
        ),
    ]
