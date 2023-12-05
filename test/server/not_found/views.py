from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def not_found(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())

def not_found_404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())