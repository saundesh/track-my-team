from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

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
    url(r'^player/teams/(?P<team_id>[0-9]+)/delete/$', views.delete_team, name='delete-team'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/roster/$', views.team_roster, name='team-roster'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/roster/(?P<player_id>[0-9]+)/$', views.player_profile, name='player-profile'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/roster/(?P<player_id>[0-9]+)/delete/$', views.delete_player, name='delete-player'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/events/$', views.team_event, name='team-events'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/events/(?P<event_id>[0-9]+)/$', views.event_details, name='event-details'),
    url(r'^player/teams/(?P<team_id>[0-9]+)/events/(?P<event_id>[0-9]+)/delete/$', views.delete_event, name='delete-event')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)