# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=False, upload_to=b''),
        ),
    ]