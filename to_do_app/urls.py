from django.urls import path
from .views import *

urlpatterns = [
    path('',homePage, name='home'),
    path('delete_post/<int:pk>/',deletePost, name='deletePost'),
    path('update_post/<int:pk>/',updatePost, name='updatePost'),
    path('add_tags/',addTag, name='add_tags'),
    path('delete_tags/<int:pk>/',deleteTags, name='delete_tags'),
]
