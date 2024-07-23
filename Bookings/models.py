from django.db import models
import uuid

class Bookings(models.Model):
    userId=models.UUIDField(  primary_key = True,default = uuid.uuid4)
    userEmail=models.EmailField(max_length = 254)
    tourName=models.CharField(null=False,max_length=254)
    fullName=models.CharField(null=False,max_length=254)
    guestSize=models.IntegerField()
    phone=models.IntegerField(max_length=10)    
    bookAt=models.DateTimeField(auto_now_add=True)
