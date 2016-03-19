# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160313_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categorie',
            field=models.CharField(default=datetime.datetime(2016, 3, 15, 14, 26, 32, 280287, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
