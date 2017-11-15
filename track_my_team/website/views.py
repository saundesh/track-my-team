# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import UserForm, TeamForm, PlayerForm, EventForm
from .models import User, Team, Player, Event

# Routes to the welcome homepage.
def index(request):
    return render(request, 'website/home.html')

# Routes to the page for users to create an account.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'website/signup.html', {'form': UserForm()})

# Routes to the page for users to log into their account.
def login(request):
    return render(request, 'website/login.html')

# Routes to the page for team captains, he/she can create a team or team roster.
def captain(request):
    return render(request, 'website/captain.html')

# Routes to the page for team captains to create a team profile.
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-team.html', {'form': TeamForm()})

# Routes to the page for team captains to create a team roster.
def create_roster(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-roster.html', {'form': PlayerForm()})

# Routes to the page for team captains to create a team roster.
def create_event(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-event.html', {'form': PlayerForm()})

# Routes to the page for players, he/she can view their team information.
def player(request):
    return render(request, 'website/player.html')

# Routes to the page for players to view their team profile.
def team_profile(request):
    data = Team.objects.all()
    all_teams = {
        "teams": data
    }
    return render(request, 'website/team-profile.html', all_teams)

# Routes to the page for players to view their team roster.
def team_roster(request):
    data = Player.objects.all()
    all_players = {
        "roster": data
    }
    return render(request, 'website/team-roster.html', all_players)

# Routes to the page for players, he/she can view their team events.
def team_events(request):
    return render(request, 'website/team-events.html')
