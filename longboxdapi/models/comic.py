from tkinter import CASCADE
from django.db import models
from .publisher import Publisher
from .character import Character
from .creator import Creator
from .team import Team
from .comic_type import ComicType


class Comic(models.Model):

    """ create a model for each comic book issue """

    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    comic_type = models.ForeignKey(ComicType, on_delete=models.CASCADE)
    series = models.CharField(max_length=50)
    characters = models.ManyToManyField(Character, through="ComicCharacter", related_name="character_in_issue")
    issue_number = models.IntegerField(null=True)
    sale_date = models.DateField()
    synopsis = models.CharField(max_length=100)
    cover_image = models.URLField()
    credits = models.ManyToManyField(Creator, through="ComicCreator", related_name="comic_creator")
    teams = models.ManyToManyField(Team, through="ComicTeam", related_name="team_in_comic")

    @property
    def inCollection(self):
        return self.__inCollection

    @inCollection.setter
    def inCollection(self, value):
        self.__inCollection = value

    @property
    def inWishlist(self):
        return self.__inWishlist

    @inWishlist.setter
    def inWishlist(self, value):
        self.__inWishlist = value