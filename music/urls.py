from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'music'
urlpatterns = [

    # /music/
    url(r'^$', views.LoginFormView.as_view(), name='login1'),
    url(r'^music$', views.indexView.as_view(), name='index'),

    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="details"),

    url(r'^song/$', views.SongView.as_view(), name="SongView"),

    url(r'song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /music/album/add/
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/album/add/
    url(r'room/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
