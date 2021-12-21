from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.ImageField(upload_to='media/')