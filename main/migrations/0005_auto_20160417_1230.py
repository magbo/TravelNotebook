# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_trip_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.upload_location),
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.upload_location),
        ),
    ]
