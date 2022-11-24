from django.urls import path
from .views_api import *

urlpatterns = [
    path('task_api/', TaskApi.as_view()),
    path('task_api/<int:pk>/', TaskApi.as_view()),
]