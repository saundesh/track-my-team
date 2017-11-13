from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^captain/$', views.captain, name='captain'),
    url(r'^captain/create-team/$', views.create_team, name='create-team'),
    url(r'^captain/create-roster/$', views.create_roster, name='create-roster'),
    url(r'^player/$', views.player, name='player'),
    url(r'^player/team/$', views.team_profile, name='team-profile'),
    url(r'^player/team/roster/$', views.team_roster, name='team-roster')
]