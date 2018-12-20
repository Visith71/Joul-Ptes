# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cffi import model
from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    price = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    room_picture = models.FileField(default=False)
    room_picture1 = models.FileField(default=False)
    room_picture2 = models.FileField(default=False)
    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + ' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    file = models.FileField(default=False)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:SongView', kwargs={})

    def __str__(self):
        return self.song_title


