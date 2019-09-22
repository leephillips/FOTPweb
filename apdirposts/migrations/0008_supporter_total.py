# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0007_auto_20190911_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='total',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
