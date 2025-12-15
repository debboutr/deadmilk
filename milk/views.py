import json

from django.http import HttpResponse, JsonResponse
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

def check(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f"{data['longitude']}, {data['latitude']}, {data['altitude']}, {data['accuracy']}")
        with open('coords.csv', 'a') as file:
            file.write(
                    f"{data['longitude']}, {data['latitude']}, {data['altitude']}, {data['accuracy'], {data['timestamp']}\n")
        return JsonResponse(data)   
    template = loader.get_template('milk/check.html')
    return HttpResponse(template.render())

