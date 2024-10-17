from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns =[
    path('',Movies,name='home'),
    path('movie/',MoviesList),
    path('movie/delete/<int:id>/',deletemovies,name = 'movies_delete'),
    path('movie/update/<int:id>/',updatemovies,name = 'movies_update')
    
]