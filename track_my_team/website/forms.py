from django import forms
from django.contrib.auth.models import User

from .models import User, Team, Player, Event

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'