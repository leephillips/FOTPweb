# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'Title: Ms., Mr., Dr., etc.', blank=True)),
                ('nameinbyline', models.CharField(max_length=200, verbose_name=b'Name in bylines', blank=True)),
                ('formalname', models.CharField(max_length=200, verbose_name=b'Formal name', blank=True)),
                ('bio', models.TextField(blank=True)),
                ('face', models.ImageField(null=True, upload_to=b'faces', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'Primary email', blank=True)),
                ('phone', models.CharField(max_length=15, verbose_name=b'Primary phone', blank=True)),
                ('notes', models.TextField(null=True, verbose_name=b'Private notes', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', null=True, editable=False, blank=True)),
                ('on', models.DateTimeField(verbose_name=b'When')),
                ('ebcode', models.CharField(max_length=400, verbose_name=b'EventBrite Code', blank=True)),
                ('publish', models.BooleanField()),
                ('content', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.ImageField(null=True, upload_to=b'illustrations', blank=True)),
                ('caption', models.TextField(blank=True)),
                ('credit', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='illustrations',
            field=models.ManyToManyField(to='apdirposts.Illustration', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('on', models.DateTimeField(null=True, verbose_name=b'When')),
                ('newslink', models.URLField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('illustrations', models.ManyToManyField(to='apdirposts.Illustration', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('byline', models.CharField(max_length=500, blank=True)),
                ('publish', models.BooleanField()),
                ('content', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('illustrations', models.ManyToManyField(to='apdirposts.Illustration', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='rpost',
            field=models.ForeignKey(blank=True, to='apdirposts.Post', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Postcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcategory', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='apdirposts.Postcategory'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Smile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('click_date', models.DateTimeField(null=True, verbose_name=b'date clicked', blank=True)),
                ('session_id', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
