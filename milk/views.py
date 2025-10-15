from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Sound, SoundCategory

def index(request):
    template = loader.get_template('milk/base.html')
    return HttpResponse(template.render())

def sound(request, category=None):
    print(category)
    if not category:
        category = "GAMESHOW"
    cats = SoundCategory.objects.all()
    sounds = Sound.objects.filter(category__name=category)
    return render(request, "milk/sound.html", {"sounds": sounds, "cats": cats})
