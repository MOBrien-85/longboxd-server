from django.db import models
from .team import Team
from .creator import Creator

class TeamCreator(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
