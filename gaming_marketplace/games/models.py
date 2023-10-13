from django.db import models

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(null = True)
    creator = models.TextField(blank=True)
    genre = models.TextField(blank=True)
    year = models.IntegerField(null = True)

