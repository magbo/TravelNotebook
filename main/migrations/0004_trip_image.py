# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160415_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]