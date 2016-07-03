from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    domain = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.domain

class Directory(models.Model):
    path = models.CharField(max_length=200)
    def __str__(self):
        return self.path

class Path(models.Model):
    path=models.CharField(max_length=200)
    def __str__(self):
        return self.path