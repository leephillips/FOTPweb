# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0010_auto_20170915_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='eclipseupload',
            name='email',
            field=models.EmailField(default='testing@example.com', max_length=75),
            preserve_default=False,
        ),
    ]
