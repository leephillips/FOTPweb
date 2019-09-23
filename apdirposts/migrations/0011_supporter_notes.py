# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0010_supporter_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='notes',
            field=models.CharField(max_length=10000, null=True, verbose_name=b'notes', blank=True),
        ),
    ]
