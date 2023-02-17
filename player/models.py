from django.db import models
import random,string

# Create your models here.

def random_number():
    length=6
    while True:
        code="".join(random.choices(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count()==0:
            break

    return code

class Room(models.Model):
    room_id=models.CharField(max_length=8,unique=True,default=random_number)
    no_players=models.IntegerField(default=0)
    created_user=models.CharField(max_length=20)
    room_status=models.BooleanField(default=True)


    def __str__(self):
        return self.room_id
class User_detail(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Password=models.CharField(max_length=20)

    def __str__(self):
        return self.Username
