from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def Connexion(request):
    template  = loader.get_template('Connexion.html')
    return HttpResponse(template.render())
