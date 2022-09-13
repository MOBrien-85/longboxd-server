from django.db import models
from .team import Team
from .creator import Creator

class Character(models.Model):

    """ create a model for each comic book character """

    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image = models.URLField()
    creators = models.ManyToManyField(Creator, through="CharacterCreator", related_name="caracter_creator")
    teams = models.ManyToManyField(Team, through="CharacterTeam", related_name="team")
