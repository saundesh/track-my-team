from django import forms
from django.contrib.auth.models import User

from .models import User, Team, Player, Event

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'sport', 'state', 'city']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'time', 'location']