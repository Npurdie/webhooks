# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_mcbot', '0002_auto_20170330_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.SlugField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
