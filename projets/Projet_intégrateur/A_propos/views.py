from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def A_propos(request):
    template  = loader.get_template('A_propos.html')
    return HttpResponse(template.render())