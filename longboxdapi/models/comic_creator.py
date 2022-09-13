from django.db import models
from .comic import Comic
from .creator import Creator

class ComicCreator(models.Model):

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
