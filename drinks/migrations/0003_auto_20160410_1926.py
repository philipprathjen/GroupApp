# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_auto_20160410_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ingredients',
            field=models.ManyToManyField(to='drinks.Ingredient'),
        ),
    ]
