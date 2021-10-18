from rest_framework import serializers
from .models import User, Item, Favorite


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = (
      'id',
      'name',
      'email',
      'phoneNumber'
    )

class ItemSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Item
    fields = (
      'id', 
      'seller',
      'title',
      'description',        
      'price',          
      'sold',            
      'condition'
    )

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    fields = (
      'items'
    )




