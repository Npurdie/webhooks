# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_mcbot', '0003_auto_20170218_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.PositiveIntegerField()),
                ('fbuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.FBUser')),
            ],
        ),
    ]
