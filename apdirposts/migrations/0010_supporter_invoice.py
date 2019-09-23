# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0009_supporter_brown_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='invoice',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Invoice number or brief description', blank=True),
        ),
    ]
