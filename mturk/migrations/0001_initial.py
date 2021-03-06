# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-11 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('annotator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullVideoTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit_id', models.CharField(blank=True, max_length=64)),
                ('hit_group', models.CharField(blank=True, max_length=64)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.Video')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
