from rest_framework import serializers
from .models import User, Item, Favorite

# how models are represented in API responses
# how data processed when creating or updating records via API reqs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'phoneNumber'
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'seller',
            'title',
            'description'
            # 'time-frame'
        )


class FavoriteSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(read_only=False, queryset= User.objects.all(), many=True)

    class Meta:
        model = Favorite
        fields = (
            'user',
            'item'
        )
