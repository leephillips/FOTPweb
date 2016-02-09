# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apdirposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', null=True, editable=False, blank=True)),
                ('on', models.DateTimeField(verbose_name=b'When')),
                ('publish', models.BooleanField()),
                ('content', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('illustrations', models.ManyToManyField(to='apdirposts.Illustration', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
