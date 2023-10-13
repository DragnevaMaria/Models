from django.db import models

# Create your models here.
class Payment (models.Model):
    username = models.CharField(max_length = 200)
    amount_money = models.IntegerField(null = True)
    # comment = models.TextField(blank=True)

