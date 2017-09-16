# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apdirposts', '0007_post_promote'),
    ]

    operations = [
        migrations.CreateModel(
            name='EclipseUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('photographer', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=500, null=True, blank=True)),
                ('file', models.ImageField(upload_to=b'eclipse')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
