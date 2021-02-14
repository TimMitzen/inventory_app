from django.db import models

# Create your models here.
class Games(models.Model):
    games = models.CharField(max_length=20)
    number_of_games = models.IntegerChoices

    date_bought = models.DateTimeField('Date game purchased')

class Type_Game(models.Model):
    type = models.ForeignKey(Games, on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
