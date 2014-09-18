# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Voter'
        db.delete_table(u'ask_voter')

        # Adding model 'VoteAnswer'
        db.create_table(u'ask_voteanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor_id', self.gf('django.db.models.fields.IntegerField')()),
            ('vote', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ans_is', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ask', ['VoteAnswer'])

        # Adding model 'VoteQuestion'
        db.create_table(u'ask_votequestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor_id', self.gf('django.db.models.fields.IntegerField')()),
            ('vote', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ques_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ask', ['VoteQuestion'])


    def backwards(self, orm):
        # Adding model 'Voter'
        db.create_table(u'ask_voter', (
            ('vote', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ask', ['Voter'])

        # Deleting model 'VoteAnswer'
        db.delete_table(u'ask_voteanswer')

        # Deleting model 'VoteQuestion'
        db.delete_table(u'ask_votequestion')


    models = {
        u'ask.answer': {
            'Meta': {'object_name': 'Answer'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_right': ('django.db.models.fields.NullBooleanField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ask.Question']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ask.question': {
            'Meta': {'object_name': 'Question'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ask.rate': {
            'Meta': {'object_name': 'Rate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'ask.voteanswer': {
            'Meta': {'object_name': 'VoteAnswer'},
            'ans_is': ('django.db.models.fields.IntegerField', [], {}),
            'autor_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vote': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ask.votequestion': {
            'Meta': {'object_name': 'VoteQuestion'},
            'autor_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ques_id': ('django.db.models.fields.IntegerField', [], {}),
            'vote': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ask']