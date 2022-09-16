"""View module for handling requests about collectors/users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Collector
from django.contrib.auth.models import User
from rest_framework.decorators import action

from longboxdapi.views.user_review import ReviewSerializer


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

    def update(self, request, pk):
        """Handle PUT requests for a user

        Returns:
            Response -- Empty body with 204 status code
        """
        # currentUser = RareUser.objects.get(user=request.auth.user)
        # if currentUser.user.is_staff is not True:
        #     return Response(None, status=status.HTTP_401_UNAUTHORIZED)
    @action(methods=['PUT'], detail=True)
    def user_active(self, request, pk):
        user = User.objects.get(pk=pk) #django
        user.is_active = not user.is_active
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')

class CollectorSerializer(serializers.ModelSerializer):
    """JSON serializer for collectors
    """
    reviews = ReviewSerializer(many=True)
    user = UserSerializer()
    class Meta: 
        model = Collector
        fields = ('id', 'user', 'bio', "reviews")

