from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def Inscription(request):
    template  = loader.get_template('Inscription.html')
    return HttpResponse(template.render())