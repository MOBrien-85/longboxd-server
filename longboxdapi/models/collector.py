from django.db import models
from django.contrib.auth.models import User
from .comic import Comic

""" importing Django user model """

class Collector(models.Model):

    """ Collector model for each user to add a bio to their profile """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    collection = models.ManyToManyField(Comic, related_name="comic_in_collection")
    wishlist = models.ManyToManyField(Comic, related_name="comic_in_wishlist")
