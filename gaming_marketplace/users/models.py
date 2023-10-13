from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length = 200)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    # models.EmailField
    email = models.TextField(blank=True)
    password = models.IntegerField(null = True)
    
