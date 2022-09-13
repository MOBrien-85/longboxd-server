"""Views module for handling requests about comic types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import ComicType


class ComicTypeView(ViewSet):
    """Longboxd comic type view"""

    def retrieve(self, request, pk):
        """handle GET requests for single issue or book

        Returns:
            Response -- JSON serialized comic type
        """
        try:
            comic_type = ComicType.objects.get(pk=pk)
            serializer = ComicTypeSerializer(comic_type)
            return Response(serializer.data)
        except ComicType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """handle GET requests to get all comic types

        Returns: 
            Response -- JSON serialized list of comic types
        """
        comic_types = ComicType.objects.all()
        serializer = ComicTypeSerializer(comic_types, many=True)
        return Response(serializer.data)


class ComicTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for comic types"""
    class Meta:
        model = ComicType
        fields = ('id', 'label')
