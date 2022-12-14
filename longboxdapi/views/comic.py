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
        collector = Collector.objects.get(user=request.auth.user)
        try:
            comic = Comic.objects.get(pk=pk)
            comic.inCollection = True if comic in collector.collection.all() else False
            comic.inWishlist = True if comic in collector.wishlist.all() else False
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

        publisher = request.query_params.get('publisher', None)
        if publisher is not None:
            comics = comics.filter(publisher_id=publisher)

        collector = Collector.objects.get(user=request.auth.user)
        for comic in comics:

            comic.inCollection = comic in collector.collection.all()

        serializer = ComicSerializer(comics, many=True)
        return Response(serializer.data)

    # i need a PUT method here so the user can add it to their wish list or collection

    @action(methods=['post'], detail=True)
    def add_comic_to_collection(self, request, pk):
        """Post request for a user to add a comic to their collection"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.objects.get(user=request.auth.user)
        collector.collection.add(comic)
        return Response({'message': 'Comic added to collection'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove_comic_from_collection(self, request, pk):
        """delete comic from the user collection"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.objects.get(user=request.auth.user)
        collector.collection.remove(comic)
        return Response({'message': 'Comic removed from collection'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def add_comic_to_wishlist(self, request, pk):
        """Post request for a user to add a comic to their wishlist"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.objects.get(user=request.auth.user)
        collector.wishlist.add(comic)
        return Response({'message': 'Comic added to wish list'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove_comic_from_wishlist(self, request, pk):
        """delete comic from the user wishlist"""

        comic = Comic.objects.get(pk=pk)
        collector = Collector.objects.get(user=request.auth.user)
        collector.wishlist.remove(comic)
        return Response({'message': 'Comic removed from wish list'}, status=status.HTTP_204_NO_CONTENT)


class ComicSerializer(serializers.ModelSerializer):
    """JSON serializer for comics
    """
    class Meta:
        model = Comic
        fields = ('id', 'title', 'publisher', 'comic_type', 'series', 'characters', 'issue_number',
                  'sale_date', 'synopsis', 'cover_image', 'credits', 'teams', 'inCollection', 'inWishlist')
        depth = 1
