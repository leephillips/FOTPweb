# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Director'
        db.create_table('apdirposts_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('nameinbyline', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('formalname', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('face', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('apdirposts', ['Director'])

        # Adding model 'Illustration'
        db.create_table('apdirposts_illustration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('credit', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('apdirposts', ['Illustration'])

        # Adding model 'Postcategory'
        db.create_table('apdirposts_postcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcategory', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('apdirposts', ['Postcategory'])

        # Adding model 'Post'
        db.create_table('apdirposts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apdirposts.Postcategory'])),
        ))
        db.send_create_signal('apdirposts', ['Post'])

        # Adding M2M table for field illustrations on 'Post'
        db.create_table('apdirposts_post_illustrations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['apdirposts.post'], null=False)),
            ('illustration', models.ForeignKey(orm['apdirposts.illustration'], null=False))
        ))
        db.create_unique('apdirposts_post_illustrations', ['post_id', 'illustration_id'])

        # Adding model 'Event'
        db.create_table('apdirposts_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('on', self.gf('django.db.models.fields.DateTimeField')()),
            ('ebcode', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('rpost', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='revent', null=True, to=orm['apdirposts.Post'])),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('apdirposts', ['Event'])

        # Adding M2M table for field illustrations on 'Event'
        db.create_table('apdirposts_event_illustrations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['apdirposts.event'], null=False)),
            ('illustration', models.ForeignKey(orm['apdirposts.illustration'], null=False))
        ))
        db.create_unique('apdirposts_event_illustrations', ['event_id', 'illustration_id'])

        # Adding model 'Notice'
        db.create_table('apdirposts_notice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('on', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('newslink', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('apdirposts', ['Notice'])

        # Adding M2M table for field illustrations on 'Notice'
        db.create_table('apdirposts_notice_illustrations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('notice', models.ForeignKey(orm['apdirposts.notice'], null=False)),
            ('illustration', models.ForeignKey(orm['apdirposts.illustration'], null=False))
        ))
        db.create_unique('apdirposts_notice_illustrations', ['notice_id', 'illustration_id'])


    def backwards(self, orm):
        
        # Deleting model 'Director'
        db.delete_table('apdirposts_director')

        # Deleting model 'Illustration'
        db.delete_table('apdirposts_illustration')

        # Deleting model 'Postcategory'
        db.delete_table('apdirposts_postcategory')

        # Deleting model 'Post'
        db.delete_table('apdirposts_post')

        # Removing M2M table for field illustrations on 'Post'
        db.delete_table('apdirposts_post_illustrations')

        # Deleting model 'Event'
        db.delete_table('apdirposts_event')

        # Removing M2M table for field illustrations on 'Event'
        db.delete_table('apdirposts_event_illustrations')

        # Deleting model 'Notice'
        db.delete_table('apdirposts_notice')

        # Removing M2M table for field illustrations on 'Notice'
        db.delete_table('apdirposts_notice_illustrations')


    models = {
        'apdirposts.director': {
            'Meta': {'object_name': 'Director'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'face': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'formalname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameinbyline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'apdirposts.event': {
            'Meta': {'object_name': 'Event'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ebcode': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['apdirposts.Illustration']", 'null': 'True', 'blank': 'True'}),
            'on': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpost': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'revent'", 'null': 'True', 'to': "orm['apdirposts.Post']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'apdirposts.illustration': {
            'Meta': {'object_name': 'Illustration'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'apdirposts.notice': {
            'Meta': {'object_name': 'Notice'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['apdirposts.Illustration']", 'null': 'True', 'blank': 'True'}),
            'newslink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'apdirposts.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apdirposts.Postcategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['apdirposts.Illustration']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'apdirposts.postcategory': {
            'Meta': {'object_name': 'Postcategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcategory': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['apdirposts']
