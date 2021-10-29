from django.urls import path
from .views import getUserFavorites, saveUserFavorites

urlpatterns = [
  path('userprofile/favorites/<str:userid>', getUserFavorites), 
  path('userprofile/newfavorite/<str:userid>', saveUserFavorites)
]