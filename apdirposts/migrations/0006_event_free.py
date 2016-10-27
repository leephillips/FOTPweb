# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0005_event_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='free',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
