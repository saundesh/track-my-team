from django import forms
from django.contrib.auth.models import User

from .models import Team, Player, Event

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=False)
    last_name = forms.CharField(label="Last Name", required=False)
    email = forms.CharField(label="Email", required=False)
    password = forms.CharField(widget=forms.PasswordInput)
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
    class Meta:
        model = Event
        fields = ['team', 'event_name', 'date', 'time', 'location']