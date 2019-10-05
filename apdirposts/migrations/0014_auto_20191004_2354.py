# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0013_supporter_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'transaction date', null=True),
        ),
    ]
