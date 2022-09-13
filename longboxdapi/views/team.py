# views for team. not yet sure how this will be used.
# maybe you can access a page for a team that lists out all characters that appear on the team at any point in it's history.
# that could be a stretch goal. for now:
# maybe just allow a character details page or comic page
# include any teams involved.

"""View module for handling requests about teams"""
import sqlite3
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from longboxdapi.models import Team


class TeamView(ViewSet):
    """longboxd team view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single team

        Returns:
            Response -- JSON serialized team
        """
        try:
            team = Team.objects.get(pk=pk)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except Team.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all teams

        Returns:
            Response -- JSON serialized list of teams
        """
        teams = Team.objects.all()
        # add filter here

        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamSerializer(serializers.ModelSerializer):
    """JSON serializer for teams"""

    class Meta:
        model = Team
        fields = ('id', 'name', 'description', 'image', 'creators')
