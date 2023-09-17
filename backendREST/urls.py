from django.contrib import admin
from django.urls import path
from .views import getUserFavorites, saveUserFavorites, createNewItem, deleteItem, createNewUser, getUserInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', createNewUser),  # root URL
    path('userprofile/favorites/<str:userid>', getUserFavorites),
    path('userprofile/newfavorite/<str:userid>', saveUserFavorites),
    path('newitem', createNewItem),
    path('item/<str:itemid>', deleteItem),
    path('userprofile/createnew', createNewUser),
    path('userprofile/<str:userid>/', getUserInfo)


]
