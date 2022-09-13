from django.db import models
from .character import Character
from .creator import Creator

class CharacterCreator(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
