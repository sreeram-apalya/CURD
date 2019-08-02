# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-21 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('hero_name', models.CharField(max_length=30)),
                ('heroine_name', models.CharField(max_length=30)),
                ('director_name', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('release_date', models.DateField(max_length=100)),
                ('budget', models.IntegerField()),
            ],
        ),
    ]