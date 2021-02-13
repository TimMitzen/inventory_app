from django.db import models

# Create your models here.
class Games(models.model):
    games = models.CharField(max_length=20)
    date_bought = models.DateTimeField('Date game purchased')

class Type_Game(models.Model):
    type = models.ForeignKey(on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
