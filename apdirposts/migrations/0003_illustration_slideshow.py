# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0002_communityevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='slideshow',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
