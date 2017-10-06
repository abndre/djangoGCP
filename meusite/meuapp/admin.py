# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Todo, Player

admin.site.register(Todo)
admin.site.register(Player)
