# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Routes to the welcome homepage.
def index(request):
    return render(request, 'website/home.html')

# Routes to the page for users to create an account.
def signup(request):
    return render(request, 'website/signup.html')

# Routes to the page for users to log into their account.
def login(request):
    return render(request, 'website/login.html')

# Routes to the page for team captains, he/she can create a team or team roster.
def captain(request):
    return render(request, 'website/captain.html')

# Routes to the page for team captains to create a team profile.
def create_team(request):
    return render(request, 'website/create-team.html')

# Routes to the page for team captains to create a team roster.
def create_roster(request):
    return render(request, 'website/create-roster.html')

# Routes to the page for players, he/she can view their team information.
def player(request):
    return render(request, 'website/player.html')

# Routes to the page for players to view their team profile.
def team_profile(request):
    return render(request, 'website/team-profile.html')

# Routes to the page for players to view their team roster.
def team_roster(request):
    return render(request, 'website/team-roster.html')