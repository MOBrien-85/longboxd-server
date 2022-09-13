from tkinter import CASCADE
from django.db import models
from .comic import Comic
from .character import Character

class ComicCharacter(models.Model):

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
