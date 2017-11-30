from django.conf import settings

from django import forms
from django.contrib.auth.models import User

import pytz, datetime
import django.utils.timezone as timezone
from django.utils.timezone import activate

from .models import Team, Player, Event

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Username'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Email Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'sport', 'state', 'city']

class UploadTeamLogoForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['avatar']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'first_name', 'last_name', 'number']

class UploadPlayerAvatarForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['avatar']

class PlayerChangeForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'first_name', 'last_name', 'number', 'email', 'phone_number', 'address', 'uin', 'usau_id']

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now)
    time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'), initial=timezone.now)
    class Meta:
        model = Event
        fields = ['team', 'event_name', 'date', 'time', 'location']