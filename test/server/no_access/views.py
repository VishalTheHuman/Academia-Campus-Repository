from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def no_access(request):
    template = loader.get_template('no_access.html')
    return HttpResponse(template.render())