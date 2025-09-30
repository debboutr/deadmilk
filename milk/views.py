from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Sound

def index(request):
    template = loader.get_template('milk/base.html')
    return HttpResponse(template.render())

def sound(request):
    sounds = Sound.objects.all()
    odd_sounds = sounds[::2]
    even_sounds = sounds[1::2]
    return render(request, "milk/sound.html", {"odd_sounds": odd_sounds,
                                               "even_sounds": even_sounds})
