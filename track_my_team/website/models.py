# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/')

# Create your models here.

# User model will store account information
class User(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.email

# Team model will store team profile information
class Team(models.Model):
    team_name = models.CharField(max_length=64)
    sport = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    avatar = models.FileField(storage=fs, upload_to='media/', default='default.png')

    def __str__(self):
        return self.team_name

# Player model will store player profile information
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=64, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=128, blank=True)
    uin = models.IntegerField(null=True, blank=True)
    usau_id = models.IntegerField(null=True, blank=True)
    avatar = models.FileField(storage=fs, upload_to='media/', default='default.png')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Event model will store player profile information
class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=64)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.event_name
