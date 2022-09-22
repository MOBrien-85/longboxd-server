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
from longboxdapi.models.collector import Collector
from longboxdapi.models import Comic
from rest_framework.decorators import action


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

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for a review
        
        Returns
            Response -- JSON serialized review instance
        """
        collector = Collector.objects.get(user=request.auth.user)
        comic = Comic.objects.get(pk=request.data["issue"])

        review = Review.objects.create(
            review=request.data["description"],
            rating=request.data["rating"],
            # favorite=request.data["favorite"],
            issue=comic,
            user=collector
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a review

        Returns:
            Response -- Empty body with 204 status code
        """
        review = Review.objects.get(pk=pk)
        review.review = request.data["description"]
        review.rating = request.data["rating"]
        # review.favorite = request.data["favorite"]

        comic = Comic.objects.get(pk=request.data["issue"])
        review.issue = comic
        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=False)
    def get_review_for_comic(self, request):
        try:
            collector = Collector.objects.get(user=request.auth.user)
            review = Review.objects.filter(issue=request.data["comic"], user=collector)
            if len(review) > 0:
                data = {"status": True, "reviewId": review[0].id}
                return Response(data)
            else: 
                data = {"status": False}
                return Response(data)
        except Review.DoesNotExist:
            return Response({})
        



class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""

    class Meta:
        model = Review
        fields = ('id', 'review', 'rating', 'issue', 'user')
        depth = 1