# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('post', '0002_auto_20171031_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='posts', to='category.Category'),
        ),
    ]
