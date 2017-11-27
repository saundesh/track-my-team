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
    class Meta:
        model = Event
        fields = ['team', 'event_name', 'date', 'time', 'location']