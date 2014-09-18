from django.db import models
# Create your models here.

from datetime import datetime

from django.contrib.auth.models import User

class Question(models.Model):
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    creation_date = models.DateField(default=datetime.now)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.header


class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    creation_date = models.DateField(default=datetime.now)
    is_right = models.NullBooleanField(default=0)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content


class Rate(models.Model):
    rating = models.IntegerField(default = 0)
    user = models.OneToOneField(User)


class VoteQuestion(models.Model):
    autor_id = models.IntegerField()
    vot = models.IntegerField(default =33)
    ques_id = models.IntegerField()


class VoteAnswer(models.Model):
    autor_id = models.IntegerField()
    vot = models.IntegerField(default = 22)
    ans_id = models.IntegerField(default = 0)


