# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 20:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_mcbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(choices=[('comp_250', 'COMP 250'), ('ecse_428', 'ECSE 428'), ('ecse_322', 'ECSE 322'), ('ecse_330', 'ECSE 330'), ('math_363', 'MATH 363')], max_length=70, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=300, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('event_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('name', models.CharField(choices=[('architecture', 'Architecture'), ('bioengineering', 'Bioengineering'), ('chemical_engineering', 'Chemical Engineering'), ('civil_engineering', 'Civil Engineering'), ('computer_engineering', 'Computer Engineering'), ('electrical_engineering', 'Electrical Engineering'), ('materials_engineering', 'Materials Engineering'), ('mechanical_engineering', 'Mechanical Engineering'), ('mining_engineering', 'Mining Engineering'), ('software_engineering', 'Software Engineering')], default='architecture', max_length=70, primary_key=True, serialize=False)),
                ('faculty', models.CharField(choices=[('engineering', 'Engineering'), ('science', 'Science'), ('arts', 'Arts'), ('education', 'Education')], default='engineering', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSociety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='fbuser',
            name='authentication_status',
            field=models.CharField(default='authentication_no', max_length=20),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='code',
            field=models.SlugField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='mcgill_email',
            field=models.EmailField(default='', max_length=254, validators=[django.core.validators.EmailValidator(message='Please enter a valid McGill email address.', whitelist='mcgill.ca')]),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='user_id',
            field=models.SlugField(default='', max_length=16, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='user_type',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='studentsociety',
            name='fbuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.FBUser'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.StudentSociety'),
        ),
        migrations.AddField(
            model_name='course',
            name='majors',
            field=models.ManyToManyField(to='fb_mcbot.Major'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='fbuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.FBUser'),
        ),
        migrations.AddField(
            model_name='admin',
            name='fbuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.FBUser'),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='courses',
            field=models.ManyToManyField(to='fb_mcbot.Course'),
        ),
        migrations.AddField(
            model_name='fbuser',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_mcbot.Major'),
        ),
    ]
