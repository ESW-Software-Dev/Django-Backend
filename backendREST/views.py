from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import User, Item, Favorite
from .serializers import UserSerializer, ItemSerializer, FavoriteSerializer
import uuid
# Create your views here.



@api_view(['GET'])
def getUserFavorites(request, userid):
  """
  returns an user's favorites. refer to API documentation for details.
  """
  try:
    User.objects.get(id=userid)
    favList = list(Favorite.objects.filter(user=userid).values())
    favInfoDict = {}
    num = 0

    for fav in favList:
      try:
        favItem = Item.objects.get(id=fav.get("item_id")) 
        favInfoDict[num] = model_to_dict(favItem)
        num = num + 1
      
      except Item.DoesNotExist:
        favInfoDict["favorite"] = "doesnotexist"

    return JsonResponse(favInfoDict)

  except User.DoesNotExist:
    fail = {
      "user":"doesnotexist"
    }
    return JsonResponse(fail)



@api_view(['PUT'])
def saveUserFavorites(request, userid):
  """
  saves an user's new favorite 
  """
  try:
    User.objects.get(id=userid)
    newFavorite = FavoriteSerializer(data=request.data)
    print(request.data)
    if newFavorite.is_valid():
      try:
        Item.objects.get(id=request.data.get("item"))
        newFavorite.save()
        return Response(newFavorite.data, status=status.HTTP_201_CREATED)
      
      except Item.DoesNotExist:
        fail = {
          "Item":"doesnotexist"
          }
        return JsonResponse(fail)
    
    #for testing ONLY
    print(newFavorite.errors)
    #f##########

    fail = {
      "user": "requestdatanotvalid",
      "item":"requestdatanotvalid"
    }
    return JsonResponse(fail)

  except User.DoesNotExist:
    fail = {
      "user":"doesnotexist"
    }
    return JsonResponse(fail)