# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0009_auto_20170915_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eclipseupload',
            old_name='iamge',
            new_name='image',
        ),
    ]
