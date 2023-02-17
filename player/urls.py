from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('create_account',views.create_account,name="create_account"),
    path('RoomPage', views.RoomPage, name="RoomPage"),
    path('join_room', views.JoinRoom, name="join_room"),

]