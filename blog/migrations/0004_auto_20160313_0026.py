# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160129_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 3, 12, 23, 26, 32, 531667, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
