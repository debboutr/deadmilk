from django.contrib import admin

from .models import SoundCategory, Sound

admin.site.register(SoundCategory)
admin.site.register(Sound)
