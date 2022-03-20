from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    response = HttpResponse('Hisame')
    return response