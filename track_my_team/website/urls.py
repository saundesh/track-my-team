from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^captain/$', views.captain, name='captain'),
    url(r'^player/$', views.player, name='player')
]