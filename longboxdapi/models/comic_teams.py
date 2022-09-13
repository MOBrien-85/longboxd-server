from django.db import models
from .comic import Comic
from .team import Team

class ComicTeam(models.Model): 

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
