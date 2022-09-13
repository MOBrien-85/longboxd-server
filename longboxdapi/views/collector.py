"""View module for handling requests about collectors/users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Collector


class CollectorView(ViewSet):
    """longboxd collector/user view for profiles"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single collector profile
        
        Returns: 
            Response -- JSON serialized collector
        """
        collector = Collector.objects.get(pk=pk)
        serializer = CollectorSerializer(collector)
        return Response(serializer.data)

class CollectorSerializer(serializers.ModelSerializer):
    """JSON serializer for collectors
    """
    class Meta: 
        model = Collector
        fields = ('id', 'user', 'bio')
