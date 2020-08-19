from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,  name="home"),
    path("ideas/", views.ideas,  name="ideas"),
    path("planning/", views.planning,  name="planning"),
    path("final/", views.final,  name="final"),
    path("video/", views.video,  name="video"),
    path("second/", views.second,  name="second_idea"),
    path("third/", views.third,  name="third_idea"),
    
]