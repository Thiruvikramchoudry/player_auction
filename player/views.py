from django.shortcuts import render,redirect
from .models import Room,User_detail
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth


# Create your views here.

def home(request):
    return render(request,"player/index.html",{"message":""})

def login(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if len(User_detail.objects.filter(Username=username,Password=password))!=0:
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/RoomPage')
        else:
            return render(request,"player/index.html",{"message":'Invalid username or password...'})

def create_account(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user_det = User_detail(Username=username, Password=password)
    user_det.save()
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return render(request, "player/index.html", {"message": 'Account Created Successfully...'})

def RoomPage(request):
    return render(request,"player/room_page.html")

def JoinRoom(request):
    
