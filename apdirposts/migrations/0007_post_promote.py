# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0006_event_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='promote',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
