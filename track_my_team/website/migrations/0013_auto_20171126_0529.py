# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 05:29
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20171126_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.FileField(default='settings.MEDIA_ROOT/default.png', storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.FileField(default='settings.MEDIA_ROOT/default.png', storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='media/'),
        ),
    ]