from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def Visualisation(request):
    template  = loader.get_template('Page_de_visualisation.html')
    return HttpResponse(template.render())