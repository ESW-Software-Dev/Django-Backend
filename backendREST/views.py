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


@api_view(['POST'])
def createNewItem(request):
    """
    creates a new post for a user
    """
    newItem = ItemSerializer(data=request.data)
    if newItem.is_valid():
        newItem.save()
        return Response(newItem.data, status=status.HTTP_201_CREATED)

    fail = {
        "item": "item is not valid"
    }
    return JsonResponse(fail)


@api_view(['DELETE'])
def deleteItem(request, itemid):
    """
    deletes a user's post
    """
    try:
        item = ItemSerializer(Item.objects.get(id=itemid))
        Item.objects.get(id=itemid).delete()
        return Response(item.data)

    except Item.DoesNotExist:
        fail = {
            "item": "item does not exist"
        }
        return JsonResponse(fail)


@api_view(['POST'])
# creates new data on the server
def createNewUser(request):
    """
    creates a new user
    """
    newUser = UserSerializer(data=request.data)
    if newUser.is_valid():
        newUser.save()
        return Response(newUser.data, status=status.HTTP_201_CREATED)

    fail = {
        "user": "user is not valid"
    }
    return JsonResponse(fail)


@api_view(['GET'])
def getUserInfo(request, userid):
    """
    Returns a dictionary of all the user profile info including their posts
    """
    try:
        user = User.objects.get(id=userid)  # Retrieve the user by ID
        user_data = UserSerializer(user).data
        return Response(user_data)
        # user = UserSerializer(User.objects.get(id=request.data.get("id")))
        # return Response(user.data)

    except User.DoesNotExist:
        fail = {
            "user": "user does not exist"
        }
        return JsonResponse(fail)


@api_view(['GET'])
# retrieving information
def getUserFavorites(request, userid):
    """
    returns an user's saved posts. refer to API documentation for details.
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
            "user": "doesnotexist"
        }
        return JsonResponse(fail)


@api_view(['PUT'])
# updating information that already exists
def saveUserFavorites(request, userid):
    """
    saves an user's saved posts
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
                    "Item": "doesnotexist"
                }
                return JsonResponse(fail)

        # for testing ONLY
        print(newFavorite.errors)
        #f##########

        fail = {
            "user": "requestdatanotvalid",
            "item": "requestdatanotvalid"
        }
        return JsonResponse(fail)

    except User.DoesNotExist:
        fail = {
            "user": "doesnotexist"
        }
        return JsonResponse(fail)
