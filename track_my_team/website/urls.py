from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^captain/$', views.captain, name='captain'),
    url(r'^player/$', views.player, name='player'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^captain/create-team/$', views.create_team, name='create-team')
]