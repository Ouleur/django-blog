# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160313_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 23, 37, 18, 739534, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 3, 12, 23, 37, 33, 96908, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
