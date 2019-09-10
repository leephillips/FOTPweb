# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0002_post_useillustration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First name')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Last name')),
                ('middle_name', models.CharField(max_length=100, null=True, verbose_name=b'Middle name', blank=True)),
                ('suffix_name', models.CharField(max_length=10, null=True, verbose_name=b'Suffix', blank=True)),
                ('purpose', models.CharField(default=1, max_length=100, verbose_name=b'What is the purpose of your payment?', choices=[(1, b'Contribution only'), (2, b'New membership'), (3, b'Renewing membership')])),
                ('member_type', models.CharField(default=1, max_length=100, verbose_name=b'Type of membership', choices=[(1, b'$15 - Individual'), (2, b'$25 - Family'), (3, b'$50 - Sponsor'), (4, b'$100 - Patron'), (5, b'$1,000 - Lifetime')])),
                ('mailing_street', models.CharField(max_length=100, null=True, verbose_name=b'Street address', blank=True)),
                ('mailing_city', models.CharField(max_length=100, null=True, verbose_name=b'City', blank=True)),
                ('mailing_state', models.CharField(max_length=100, null=True, verbose_name=b'State or province', blank=True)),
                ('mailing_zip', models.CharField(max_length=30, null=True, verbose_name=b'Zip or postal code', blank=True)),
                ('phone', models.CharField(max_length=30, null=True, verbose_name=b'Phone number', blank=True)),
                ('phone_type', models.CharField(default=1, choices=[(1, b'Mobile'), (2, b'Home'), (3, b'Work')], max_length=20, blank=True, null=True, verbose_name=b'Type')),
                ('wants_email', models.BooleanField(default=False)),
                ('comments', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
