# user reviews will be handled here
# GET functions -- LIST so i can populate all reviews on a user's profile
# this will also need to include filters
# also a RETRIEVE method to grab just one at a time
# this will also need
# CREATE -- for creating a review
# and UPDATE -- for editing a review
# and then custom actions for POST to the db
# and then DELETE method


"""View module for handling requests about user reviews"""
import sqlite3
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Review


class ReviewView(ViewSet):
    """longboxd review view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single review

        Returns:
            Response -- JSON serialized review
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()
        # add filter here

        serializer = TeamSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""

    class Meta:
        model = Review
        fields = ('id', 'review', 'rating', 'favorite', 'issue', 'user')
