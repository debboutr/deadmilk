from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
  template = loader.get_template('milk/base.html')
  return HttpResponse(template.render())

def sound(request):
  return render(request, "milk/sound.html")
