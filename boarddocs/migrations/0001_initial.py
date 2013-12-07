# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Boardfile'
        db.create_table('boarddocs_boardfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('covering', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('boarddocs', ['Boardfile'])

        # Adding model 'Annualreport'
        db.create_table('boarddocs_annualreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('boarddocs', ['Annualreport'])

        # Adding model 'Budgetreport'
        db.create_table('boarddocs_budgetreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('boarddocs', ['Budgetreport'])

        # Adding model 'Minutes'
        db.create_table('boarddocs_minutes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('meetingDate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('boarddocs', ['Minutes'])

        # Adding model 'Agenda'
        db.create_table('boarddocs_agenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('meetingDate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('boarddocs', ['Agenda'])

        # Adding model 'Historical'
        db.create_table('boarddocs_historical', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whenUploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('thefile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
        ))
        db.send_create_signal('boarddocs', ['Historical'])


    def backwards(self, orm):
        
        # Deleting model 'Boardfile'
        db.delete_table('boarddocs_boardfile')

        # Deleting model 'Annualreport'
        db.delete_table('boarddocs_annualreport')

        # Deleting model 'Budgetreport'
        db.delete_table('boarddocs_budgetreport')

        # Deleting model 'Minutes'
        db.delete_table('boarddocs_minutes')

        # Deleting model 'Agenda'
        db.delete_table('boarddocs_agenda')

        # Deleting model 'Historical'
        db.delete_table('boarddocs_historical')


    models = {
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
        'boarddocs.agenda': {
            'Meta': {'object_name': 'Agenda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meetingDate': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'boarddocs.annualreport': {
            'Meta': {'object_name': 'Annualreport'},
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'boarddocs.boardfile': {
            'Meta': {'object_name': 'Boardfile'},
            'covering': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'boarddocs.budgetreport': {
            'Meta': {'object_name': 'Budgetreport'},
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'boarddocs.historical': {
            'Meta': {'object_name': 'Historical'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'boarddocs.minutes': {
            'Meta': {'object_name': 'Minutes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meetingDate': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'thefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'whenUploaded': ('django.db.models.fields.DateTimeField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['boarddocs']
