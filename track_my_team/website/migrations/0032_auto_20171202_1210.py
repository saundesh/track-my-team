# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
