from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class User(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
   
    # items = a list of items
    phoneNumber = models.IntegerField(max_length = 20)
    # Picture (media file)
    # Favorites [items]

def __str__(self):
    return self.email


class Item(models.Model):
    id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    # seller = User
    sold = models.BooleanField(default=False)
    condition = models.CharField(max_length=20)
    
# def __str__(self):
    # return self.id, self.title

# class Category(models.Model):
