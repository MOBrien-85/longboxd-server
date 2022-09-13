from django.db import models
from .creator import Creator

class Team(models.Model):

    """ create a model for each 
    comic book team """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.URLField()
    creators = models.ManyToManyField(Creator, through="TeamCreator", related_name="team_creator")
