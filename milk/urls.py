from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sounds/", views.sound, name="sounds"),
    path("sounds/<slug:category>/", views.sound, name="sounds"),
    path("work/", views.work, name="work"),
]
