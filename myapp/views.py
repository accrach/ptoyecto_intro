from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello (request):

    return HttpResponse("<h1>hello world</h1>")

def prueba (request):

    return HttpResponse('probando la nueva parte de la pagina')

