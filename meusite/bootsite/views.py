# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Jogador

def index(request):
    #return HttpResponse("Hello, world")
    return render(request, 'index.html')

def menuplayer(request,id):

    jogado = Jogador.objects.get(id=id)
    context = {
        'jogado':jogado
    }
    return render (request, 'details.html',context)


def menu(request):
    jogadores = Jogador.objects.all()#[:10]
    context = {
        'jogadores':jogadores
    }
    return render (request, 'players.html',context)
