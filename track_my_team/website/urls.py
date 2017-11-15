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
    url(r'^captain/create-team/submit/$', views.create_team, name='create-team-submit'),
    url(r'^captain/create-roster/$', views.create_roster, name='create-roster'),
    url(r'^captain/create-roster/submit/$', views.create_team, name='create-roster-submit'),
    url(r'^captain/create-event/$', views.create_event, name='create-event'),
    url(r'^captain/create-event/submit/$', views.create_event, name='create-event-submit'),
    url(r'^player/$', views.player, name='player'),
    url(r'^player/team/$', views.team_profile, name='team-profile'),
    url(r'^player/team/roster/$', views.team_roster, name='team-roster'),
    url(r'^player/team/events/$', views.team_event, name='team-events')
]