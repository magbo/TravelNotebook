# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-02 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_tag_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='geom',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='geom',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
