from django.urls import path
from .views import getUserFavorites, saveUserFavorites, createNewItem, deleteItem, createNewUser, getUserInfo

urlpatterns = [
  path('userprofile/favorites/<str:userid>', getUserFavorites), 
  path('userprofile/newfavorite/<str:userid>', saveUserFavorites),
  path('newitem', createNewItem),
  path('item/<str:itemid>', deleteItem),
  path('userprofile/createnew', createNewUser),
  path('userprofile', getUserInfo)

]