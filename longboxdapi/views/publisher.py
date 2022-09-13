# views for publishers
# GET -- list all publishers
# retrieve a single publisher

"""View module for handling requests about publishers"""
import sqlite3
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Publisher


class PublisherView(ViewSet):
    """longboxd publishers view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single publisher

        Returns:
            Response -- JSON serialized publisher
        """
        try:
            publisher = Publisher.objects.get(pk=pk)
            serializer = PublisherSerializer(publisher)
            return Response(serializer.data)
        except Publisher.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all publishers

        Returns:
            Response -- JSON serialized list of publishers
        """
        publishers = Publisher.objects.all()
        # add filtering here if need be
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)


class PublisherSerializer(serializers.ModelSerializer):
    """JSON serializer for publishers"""

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'founded', 'description', 'image')
