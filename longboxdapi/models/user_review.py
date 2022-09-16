from django.db import models
from .comic import Comic
from .collector import Collector


class Review(models.Model):

    """ create a model for each user
    review of a 
    comic book issue or 
    trade paperback """

    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    issue = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name="reviews")
