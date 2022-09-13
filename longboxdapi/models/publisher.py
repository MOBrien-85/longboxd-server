from django.db import models

class Publisher(models.Model):

    """ create a model for each 
    comic book publisher """

    name = models.CharField(max_length=50)
    founded = models.CharField(max_length=4)
    description = models.CharField(max_length=100)
    image = models.URLField()
