# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180525_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default=False, upload_to=b''),
        ),
    ]