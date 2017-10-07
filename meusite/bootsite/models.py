# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class Jogador(models.Model):
    nome        = models.CharField(max_length=200)
    level       = models.IntegerField(default=1)
    xp          = models.IntegerField(default=0)
    ataque      = models.IntegerField(default=10)
    defese      = models.IntegerField(default=10)
    genre      = models.IntegerField(default=1)
    creat_at    =  models.DateTimeField(default = datetime.now, blank = True)


    def __str__(self):
        return self.nome
