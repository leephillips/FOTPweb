# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0005_supporter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='purpose',
            field=models.CharField(default=1, max_length=100, verbose_name=b'What is the purpose of your payment?', choices=[(2, b'New membership'), (3, b'Renewing membership')]),
        ),
    ]
