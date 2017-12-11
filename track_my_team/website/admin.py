# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Team, Player, Event, Announcement

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'sport', 'state', 'city')

admin.site.register(Team, TeamAdmin)



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'number', 'name', 'role', 'team')

    def name(self, obj):
        return obj.first_name + ' ' + obj.last_name
        
admin.site.register(Player, PlayerAdmin)



class EventAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'event_name', 'team')
    
admin.site.register(Event, EventAdmin)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'title', 'team')
    
admin.site.register(Announcement, AnnouncementAdmin)