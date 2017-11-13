# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'website/home.html')

def signup(request):
    return render(request, 'website/signup.html')

def login(request):
    return render(request, 'website/login.html')

def captain(request):
    return render(request, 'website/captain.html')

def create_team(request):
    return render(request, 'website/create-team.html')

def create_roster(request):
    return render(request, 'website/create-roster.html')

def player(request):
    return render(request, 'website/player.html')

def team_profile(request):
    return render(request, 'website/team-profile.html')

def team_roster(request):
    return render(request, 'website/team-roster.html')