# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0012_auto_20190923_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='date',
            field=models.DateTimeField(verbose_name=b'transaction date', null=True, editable=False, blank=True),
        ),
    ]
