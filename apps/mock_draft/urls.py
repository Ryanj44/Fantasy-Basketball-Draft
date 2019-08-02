from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_team$', views.create_team),
    url(r'^draft$', views.draft),
    url(r'^draft/pg$', views.point),
    url(r'^draft/sg$', views.shooting),
    url(r'^draft/sf$', views.small),
    url(r'^draft/pf$', views.power),
    url(r'^draft/c$', views.center),
    url(r'^draft/(?P<player_id>\d+)$', views.add_player),
    url(r'^results$', views.results),
    url(r'^team/(?P<team_id>\d+)$', views.team)
]