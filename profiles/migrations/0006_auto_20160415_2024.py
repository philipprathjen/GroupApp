# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160415_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_cocktail',
            name='liked',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='templates/profile_images/<function upload_location at 0x103cc2048>'),
        ),
    ]
