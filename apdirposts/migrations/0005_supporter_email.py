# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0004_supporter_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Primary email', blank=True),
        ),
    ]
