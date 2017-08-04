# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170707_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('b', models.IntegerField()),
                ('c', models.IntegerField()),
                ('v', models.IntegerField()),
                ('t', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('chapter_number', models.IntegerField()),
                ('no_of_verses', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='no_of_chapters',
            field=models.IntegerField(),
        ),
    ]