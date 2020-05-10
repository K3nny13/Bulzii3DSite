from django.db import models

# Create your models here.

class Artwork(models.Model):
    title = models.CharField(max_length=40)
    image_url = models.CharField(max_length=350)
    description = models.CharField(max_length=300)

    def __str__(self):
        return this.title