from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def hello(request):
    t=Template('<h1>he he {{name}}</h1>')
    c=Context({'name':'Rudzeris'})
    return HttpResponse(t.render(context=c))