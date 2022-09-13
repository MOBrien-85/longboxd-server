from django.db import models

class ComicType(models.Model):

    """ create a model for each comic book type """

    label = models.CharField(max_length=50)
