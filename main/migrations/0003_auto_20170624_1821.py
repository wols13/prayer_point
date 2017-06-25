# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170102_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayer_point',
            name='book',
            field=models.CharField(default='no_book', max_length=20),
        ),
        migrations.AddField(
            model_name='prayer_point',
            name='chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prayer_point',
            name='verse',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prayer_point',
            name='content',
            field=models.TextField(default='no_content', max_length=512),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='book',
            field=models.CharField(max_length=20),
        ),
    ]
