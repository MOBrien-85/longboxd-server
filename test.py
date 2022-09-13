# import mokkari
# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from longboxdapi.models import Character

# class CharacterView(ViewSet):
#     """longboxd character view"""

#     def retrieve(self, request, pk):
#         """handle GET requests for a single character

#         Returns: 
#             Response -- JSON serialized character
#         """
#         try: 
#             character = Character.objects.get(pk=pk)
#             serializer = CharacterSerializer(character)
#             return Response(serializer.data)
#         except Character.DoesNotExist as ex:
#             return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# class CharacterSerializer(serializers.ModelSerializer):
#     """JSON serializer for characters"""
#     class Meta:
#         model = Character
#         fields = ('id', 'name', 'alias', 'desc', 'image',
#                     'creators', 'teams', 'modified')


import mokkari

# Your own config file to keep your credentials secret
# from config import username, password

m = mokkari.api("obiethered", "Y@nkees1985")

# Get all Marvel comics for the week of 2021-06-07
this_week = m.issues_list({"store_date_range_after": "2021-06-07", "store_date_range_before": "2021-06-13", "publisher_name": "marvel"})

# Print the results
for i in this_week:
    print(f"{i.id} {i.issue_name}")

# Retrieve the detail for an individual issue
asm_68 = m.issue(31660)

# Print the issue Description
print(asm_68.desc)