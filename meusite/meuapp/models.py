# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Todo(models.Model):
    title        = models.CharField(max_length=200)
    text         = models.TextField()
    creat_at     =  models.DateTimeField(default = datetime.now, blank = True)


    def __str__(self):
        return self.title



class Player(models.Model):
    name        = models.CharField(max_length=200)
    level       = models.IntegerField()
    xp          = models.IntegerField()
    ataque      = models.IntegerField()
    defese      = models.IntegerField()
    creat_at    =  models.DateTimeField(default = datetime.now, blank = True)


    def __str__(self):
        return self.name
