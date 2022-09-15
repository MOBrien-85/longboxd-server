"""View module for handling requests about comics"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from longboxdapi.models import Comic
from longboxdapi.models import Collector


class ComicView(ViewSet):
    """Longboxd comics view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comic

        Returns:
            Response -- JSON serialized comic
        """
        try:
            comic = Comic.objects.get(pk=pk)
            serializer = ComicSerializer(comic)
            return Response(serializer.data)
        except Comic.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all comics

        Returns: 
            Response -- JSON serialized list of all comics
        """
        comics = Comic.objects.all()

        comic_type = request.query_params.get('type', None)
        if comic_type is not None:
            comics = comics.filter(comic_type_id=comic_type)

        serializer = ComicSerializer(comics, many=True)
        return Response(serializer.data)

    # i need a PUT method here so the user can add it to their wish list or collection

    @action(methods=['post'], detail=True)
    def addComicToCollection(self, request, pk):
        """Post request for a user to add a comic to their collection"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.get(user=request.auth.user)
        collector.collection.add(comic)
        return Response({'message': 'Comic added to collection'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeComicFromCollection(self, request, pk):
        """delete comic from the user collection"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.get(user=request.auth.user)
        collector.collection.remove(comic)
        return Response({'message': 'Comic removed from collection'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def addComicToWishlist(self, request, pk):
        """Post request for a user to add a comic to their wishlist"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.get(user=request.auth.user)
        collector.wishlist.add(comic)
        return Response({'message': 'Comic added to wish list'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeComicFromWishlist(self, request, pk):
        """delete comic from the user wishlist"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.get(user=request.auth.user)
        collector.wishlist.remove(comic)
        return Response({'message': 'Comic removed from wish list'}, status=status.HTTP_204_NO_CONTENT)


class ComicSerializer(serializers.ModelSerializer):
    """JSON serializer for comics
    """
    class Meta:
        model = Comic
        fields = ('id', 'title', 'publisher', 'comic_type', 'series', 'characters', 'issue_number',
                  'sale_date', 'synopsis', 'cover_image', 'credits', 'teams')
        depth = 1
