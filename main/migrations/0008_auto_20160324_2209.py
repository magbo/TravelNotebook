# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160310_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]