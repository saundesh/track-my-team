# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Team, Player, Event

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'sport')

admin.site.register(Team, TeamAdmin)



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'team')

    def name(self, obj):
        return obj.first_name + ' ' + obj.last_name
        
admin.site.register(Player, PlayerAdmin)



class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'event_name', 'team')
    
admin.site.register(Event, EventAdmin)