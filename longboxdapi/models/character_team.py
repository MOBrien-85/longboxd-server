from django.db import models
from .character import Character
from .team import Team

class CharacterTeam(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
