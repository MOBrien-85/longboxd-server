from django.db import models

class Creator(models.Model):

    """ create a model for each comic book creator """

    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    image = models.URLField()
