# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0008_eclipseupload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eclipseupload',
            old_name='file',
            new_name='iamge',
        ),
    ]
