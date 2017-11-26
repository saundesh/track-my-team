# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-team.html', {'form': TeamForm()})

# Routes to the page for team captains to create a team roster.
def create_roster(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-roster.html', {'form': PlayerForm()})

# Routes to the page for team captains to create a team roster.
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'website/create-event.html', {'form': EventForm()})

# Routes to the page for players, he/she can view their team information.
def player(request):
    return render(request, 'website/player.html')

# Routes to the page for players to view a list of their teams.
def team_list(request):
    teams = Team.objects.all()
    all_teams = { "teams": teams }
    return render(request, 'website/team-list.html', all_teams)

# Routes to the page for players to view each team profile.
def team_profile(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'website/team-profile.html', { "team": team })

# Routes to the page for players to view their team rosters.
def team_roster(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = Player.objects.filter(team=team_id)
    all_players = { "roster": players }
    return render(request, 'website/team-roster.html', all_players)

# Routes to the page for players to view each player profile.
def player_profile(request, team_id, player_id):
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'website/player-profile.html', { "player": player })

# Routes to the page for players, he/she can view their team events.
def team_event(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    events = Event.objects.filter(team=team_id)
    all_events = { "events": events }
    return render(request, 'website/team-event.html', all_events)

# Routes to the page for players, he/she can view details for each team event.
def event_details(request, team_id, event_id):
    team = get_object_or_404(Team, pk=team_id)
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'website/event-details.html', { "event": event })
