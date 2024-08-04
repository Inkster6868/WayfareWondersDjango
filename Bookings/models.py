from django.db import models
import uuid
from api_auth.models import User

class Bookings(models.Model):
    user_id=models.ForeignKey(User, related_name="bookings",on_delete=models.CASCADE)
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    userEmail=models.EmailField(max_length = 254)
    tourName=models.CharField(null=False,max_length=254)
    fullName=models.CharField(null=False,max_length=254)
    guestSize=models.IntegerField()
    phone=models.IntegerField(max_length=10)    
    bookAt=models.DateTimeField(auto_now_add=True)
