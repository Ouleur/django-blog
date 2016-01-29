# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_biographie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biographie',
            name='contenu',
            field=models.TextField(),
        ),
    ]
