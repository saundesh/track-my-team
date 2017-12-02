# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import UserForm, TeamForm, UploadTeamAvatarForm, PlayerForm, UploadPlayerAvatarForm, PlayerChangeForm, EventForm
from .models import Team, Player, Event

### HOME PAGE

# Routes to the welcome homepage.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        return render(request, 'website/home.html')

### USER REGISTRATION: SIGNUP AND LOGIN

# Routes to the page for users to create an account.
def signup(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    return render(request, 'website/signup.html', { "form": form })

# Routes to the page for users to log into their account.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                teams = Team.objects.filter(user=request.user)
                return render(request, 'website/team-list.html', { "teams": teams })
        else:
            return render(request, 'website/login.html', { 'error_message': 'Invalid Login' })
    return render(request, 'website/login.html')

# Routes to the page for users to log out of their account.
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'website/login.html', { "form": form })

### USER TYPE: CAPTAIN OR PLAYER

# Routes to the page for team captains, he/she can create a team or team roster.
def captain(request):
    return render(request, 'website/captain.html')

# Routes to the page for players, he/she can view their team information.
def player(request):
    return render(request, 'website/player.html')

### TEAM: CREATE, VIEW, EDIT, DELETE

# Routes to the page for team captains to create a team profile.
def create_team(request):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        form = TeamForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                team = form.save(commit=False)
                team.user = request.user
                team.save()
                return HttpResponseRedirect('/player/teams/')
        return render(request, 'website/create-team.html', { "form": form })

# Routes to the page for players to view a list of their teams.
def team_list(request):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        teams = Team.objects.filter(user=request.user)
        return render(request, 'website/team-list.html', { "teams": teams })

# Routes to the page for players to view each team profile.
def team_profile(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        return render(request, 'website/team-profile.html', { "team": team })

# Routes to the page for team captains to upload a team logo.
def upload_team_avatar(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        form = UploadTeamAvatarForm(request.POST or None, request.FILES or None, instance=team)
        if request.method == 'POST':
            if form.is_valid():
                team = form.save(commit=False)
                team.save()
                return HttpResponseRedirect('/player/teams/' + team_id)
        return render(request, 'website/upload-avatar.html', { "form": form })

# Routes to the page for team captains to edit the team profile.
def edit_team(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        form = TeamForm(request.POST or None, instance=team)
        if request.method == 'POST':
            if form.is_valid():
                team = form.save(commit=False)
                team.save()
                return HttpResponseRedirect('/player/teams/' + team_id)
        return render(request, 'website/edit-team.html', { "form": form })

# Routes to the list of teams page with specified team deleted.
def delete_team(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = Team.objects.get(pk=team_id)
        team.delete()
        teams = Team.objects.filter(user=request.user)
        return render(request, 'website/team-list.html', { "teams": teams })

### PLAYER: CREATE, VIEW, EDIT, DELETE

# Routes to the page for team captains to create a team roster.
def create_roster(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        form = PlayerForm(request.POST or None, request.FILES or None)
        form.fields['team'].queryset = Team.objects.filter(user=request.user)
        form.fields['team'].initial = team_id
        if request.method == 'POST':
            if form.is_valid():
                player = form.save(commit=False)
                player.save()
            return HttpResponseRedirect('/player/teams/' + request.POST['team'] + '/roster/')
        return render(request, 'website/create-roster.html', { "form": form })

# Routes to the page for players to view their team rosters.
def team_roster(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        players = Player.objects.filter(team=team_id).order_by('number')
        return render(request, 'website/team-roster.html', { "team": team, "roster": players })

# Routes to the page for players to view each player profile.
def player_profile(request, team_id, player_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        player = get_object_or_404(Player, pk=player_id)
        return render(request, 'website/player-profile.html', { "player": player })

# Routes to the page for players to upload a profile picture.
def upload_player_avatar(request, team_id, player_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        player = get_object_or_404(Player, pk=player_id)
        form = UploadPlayerAvatarForm(request.POST or None, request.FILES or None, instance=player)
        if request.method == 'POST':
            if form.is_valid():
                player = form.save(commit=False)
                player.save()
                return HttpResponseRedirect('/player/teams/' + team_id + '/roster/' + player_id)
        return render(request, 'website/upload-avatar.html', { "form": form })

# Routes to the page for players to edit their profile.
def edit_player(request, team_id, player_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        player = get_object_or_404(Player, pk=player_id)
        form = PlayerChangeForm(request.POST or None, request.FILES or None, instance=player)
        if request.method == 'POST':
            if form.is_valid():
                player = form.save(commit=False)
                player.save()
                return HttpResponseRedirect('/player/teams/' + team_id + '/roster/' + player_id)
        return render(request, 'website/edit-player.html', { "form": form })

# Routes to the team roster page with specified player deleted.
def delete_player(request, team_id, player_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        player = Player.objects.get(pk=player_id)
        player.delete()
        players = Player.objects.filter(team=team_id).order_by('number')
        return render(request, 'website/team-roster.html', { "roster": players })

### EVENT: CREATE, VIEW, EDIT, DELETE

# Routes to the page for team captains to create a team roster.
def create_event(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        form = EventForm(request.POST or None)
        form.fields['team'].queryset = Team.objects.filter(user=request.user)
        if request.method == 'POST':
            if form.is_valid():
                event = form.save(commit=False)
                event.save()
                return HttpResponseRedirect('/player/teams/' + request.POST['team'] + '/events/')
        return render(request, 'website/create-event.html', { "form": form })

# Routes to the page for players, he/she can view their team events.
def team_event(request, team_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        events = Event.objects.filter(team=team_id).order_by('date')
        return render(request, 'website/team-event.html', { "team": team, "events": events })

# Routes to the page for players, he/she can view details for each team event.
def event_details(request, team_id, event_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'website/event-details.html', { "event": event })

# Routes to the page for team captains to edit their profile.
def edit_event(request, team_id, event_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        event = get_object_or_404(Event, pk=event_id)
        form = EventForm(request.POST or None, instance=event)
        if request.method == 'POST':
            if form.is_valid():
                event = form.save(commit=False)
                event.save()
                return HttpResponseRedirect('/player/teams/' + team_id + '/events/' + event_id)
        return render(request, 'website/edit-event.html', { "form": form })

# Routes to the event page with specified event deleted.
def delete_event(request, team_id, event_id):
    if not request.user.is_authenticated():
        return render(request, 'website/login.html')
    else:
        team = get_object_or_404(Team, pk=team_id)
        event = Event.objects.get(pk=event_id)
        event.delete()
        events = Event.objects.filter(team=team_id).order_by('date')
        return render(request, 'website/team-event.html', { "events": events })
