from django.db import models

# Create your models here.
XBOX_ONE = "XBOX1"
PLAYSTATION_THREE = 'PS3'
PLAYSTATION_FOUR = 'PS4'
NINTENDO_SWITCH = 'SWITCH'
COMPUTER = 'PC'

LIKED = 'Liked'
OKAY = 'OK'
NOT_LIKED = "Not Liked"

SYSTEM_TYPE = ((XBOX_ONE,'XBOX1'),
               (PLAYSTATION_FOUR, 'PS4'),
               (PLAYSTATION_THREE,'PS3'),
               (NINTENDO_SWITCH, 'SWITCH'),
               (COMPUTER, 'PC'))
GAME_OPINION = ((LIKED, 'Liked'),
                (OKAY, 'OK'),
                (NOT_LIKED, 'Not Liked'))

class Games(models.Model):
    game_name = models.CharField(max_length=20, blank=False, null=True)
    game_type = models.CharField(max_length=20, blank=False, null=True)
    game_system = models.CharField(max_length= 20,choices=SYSTEM_TYPE, null = True)
    how_much_liked = models.CharField(max_length= 20, choices=GAME_OPINION, null=True)

class Type_Game(models.Model):
    type = models.ForeignKey(Games, on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
