# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_team_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
    ]
