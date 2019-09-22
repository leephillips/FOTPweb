# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0008_supporter_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='brown_donation',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
