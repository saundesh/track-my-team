# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20171126_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.FileField(default='default.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.FileField(default='default.png', upload_to='media/'),
        ),
    ]