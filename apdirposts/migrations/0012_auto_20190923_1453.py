# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0011_supporter_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='amount',
            field=models.DecimalField(null=True, verbose_name=b'Amount in $U.S.', max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='supporter',
            name='status',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Status', blank=True),
        ),
        migrations.AddField(
            model_name='supporter',
            name='transactioncode',
            field=models.CharField(max_length=100, verbose_name=b'Transaction code', blank=True),
        ),
    ]
