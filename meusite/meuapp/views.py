# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from .models import Todo
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world")
    return render(request, 'meuapp/index.html')

def post_list(request):
    return render(request, 'meuapp/post_list.html', {})


def blog(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos':todos
    }
    return render (request, 'meuapp/blog.html',context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render (request, 'meuapp/details.html',context)
