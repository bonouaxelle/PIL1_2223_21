from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def index(request):
    template  = loader.get_template('index.html')
    data ={'age' : 19}
    return HttpResponse(template.render(data))