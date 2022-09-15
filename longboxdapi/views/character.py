# Character GET functions go here.
# this will include a LIST and a RETRIEVE method
"""View module for handling requests about characters"""
import sqlite3
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Character, Team, Creator


class CharacterView(ViewSet):
    """longboxd characters view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single character

        Returns:
            Response -- JSON serialized character
        """
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all characters

        Returns:
            Response -- JSON serialized list of characters
        """
        characters = Character.objects.all()
        # do i want to add a filter here? filter by creator or team?

        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)


class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters"""
    class Meta:
        model = Character
        fields = ('id', 'name', 'desc', 'image', 'creators', 'teams')
        depth = 2
