from rest_framework import serializers
from .models import User, Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id', 
            'title', 
            'description', 
            'price', 
            'seller', 
            'sold',
        )

# class SecretUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User

