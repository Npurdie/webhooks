# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_mcbot', '0005_auto_20170219_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbuser',
            name='timezone',
            field=models.IntegerField(default=-5),
        ),
    ]