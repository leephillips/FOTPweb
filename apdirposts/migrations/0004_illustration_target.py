# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0003_illustration_slideshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='target',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
