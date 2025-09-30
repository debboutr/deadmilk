from django.db import models

class SoundCategory(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Sound(models.Model):
    emoji = models.CharField(max_length=30)
    file = models.FileField(upload_to="uploads/")
    category = models.ForeignKey(SoundCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.emoji
