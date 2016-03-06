from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=120, blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    votes = models.IntegerField()

    def __unicode__(self): #Python3.3 is __str__
        return self.email

class Answer(models.Model):
    answer = models.TextField(blank=True, null=True)
    author = models.OneToOneField(User, primary_key=True)
    published_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    votes = models.IntegerField()
