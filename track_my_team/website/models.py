# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    country = models.CharField(max_length=64)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.team_name

# Player model will store player profile information
class Player(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Event model will store player profile information
class Event(models.Model):
    event_name = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.event_name
