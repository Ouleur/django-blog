# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160313_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='nom',
            new_name='mail',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='objet',
            field=models.CharField(default=datetime.datetime(2016, 3, 13, 1, 33, 6, 474629, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]
