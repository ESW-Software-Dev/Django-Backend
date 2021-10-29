from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    phoneNumber = models.IntegerField()
    #profile pic = media file - to be config later

    def __str__(self):
        return self.email


class Item(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    seller = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    sold = models.BooleanField(default=False)
    condition = models.CharField(max_length=20)
    #pic = media file - to be config later

    def __str__(self):
        return f"title: {self.title}, seller: {self.seller}"

class Favorite(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"user: {self.user}, item: {self.item}"
    
