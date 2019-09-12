# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0006_auto_20190910_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='member_type',
            field=models.CharField(default=b'Nomembership', max_length=100, verbose_name=b'Type of membership', choices=[(b'Nomembership', b'I am not purchasing a membership.'), (b'Individual', b'$15 - Individual'), (b'Family', b'$25 - Family'), (b'Sponsor', b'$50 - Sponsor'), (b'Patron', b'$100 - Patron'), (b'Lifetime', b'$1,000 - Lifetime')]),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='phone_type',
            field=models.CharField(default=b'Mobile', choices=[(b'Mobile', b'Mobile'), (b'Home', b'Home'), (b'Work', b'Work')], max_length=20, blank=True, null=True, verbose_name=b'Type'),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='purpose',
            field=models.CharField(default=b'New', max_length=100, verbose_name=b'What is the purpose of your payment?', choices=[(b'New', b'New membership'), (b'Renewing', b'Renewing membership')]),
        ),
    ]
