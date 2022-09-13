"""View module for handling requests about collectors/users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Creator


class CreatorView(ViewSet):
    """longboxd creator view for profiles"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single creator profile
        
        Returns: 
            Response -- JSON serialized creator
        """
        creator = Creator.objects.get(pk=pk)
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)

class CreatorSerializer(serializers.ModelSerializer):
    """JSON serializer for collectors
    """
    class Meta: 
        model = Creator
        fields = ('id', 'name', 'bio', 'image')
