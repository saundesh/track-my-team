from django.conf.urls import url

from . import views

# Create all the routes found in views. Each method in views links to a html template.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup/submit/$', views.signup, name='signup-submit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^captain/$', views.captain, name='captain'),
    url(r'^captain/create-team/$', views.create_team, name='create-team'),
    url(r'^captain/create-roster/$', views.create_roster, name='create-roster'),
    url(r'^captain/create-event/$', views.create_event, name='create-event'),
    url(r'^player/$', views.player, name='player'),
    url(r'^player/teams/$', views.team_list, name='team-list'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/$', views.team_profile, name='team-profile'),
    url(r'^player/teams/roster/$', views.team_roster, name='team-roster'),
    url(r'^player/teams/roster/(?P<player_id>[0-9]+)/$', views.player_profile, name='player-profile'),
    url(r'^player/teams/events/$', views.team_event, name='team-events')
]