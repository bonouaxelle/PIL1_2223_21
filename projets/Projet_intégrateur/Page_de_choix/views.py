from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def Choix(request):
    template  = loader.get_template('Page_de_choix.html')
    return HttpResponse(template.render())