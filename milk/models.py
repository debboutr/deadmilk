from django.db import models

class CustomQuerySet(models.QuerySet):
    def odd_sounds(self):
        return self.annotate(
                odd=models.F('pk') % 2).filter(odd=True)
    def even_sounds(self):
        return self.annotate(
                odd=models.F('pk') % 2).filter(odd=False)

class SoundCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name

class Sound(models.Model):
    title = models.CharField(max_length=47, unique=True)
    file = models.FileField(upload_to="uploads/")
    category = models.ForeignKey(SoundCategory,
                                 on_delete=models.CASCADE)
    objects = CustomQuerySet.as_manager()
    def __str__(self):
        return self.title
    def name(self):
        return self.file.name.split("/")[1].split(".")[0]



