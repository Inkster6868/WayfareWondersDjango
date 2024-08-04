from django.db import models
from api_auth.models import User
import uuid

class Tour(models.Model):
    tour_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(
        max_length=255
    )  
    city = models.CharField(
        max_length=255
    ) 
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  
    photo = models.ImageField(upload_to="tour-images/")  
    address = models.CharField(max_length=255) 
    distance = models.PositiveIntegerField()  
    max_group_size = (
        models.PositiveIntegerField()
    )  
    desc = models.TextField() 
    featured = models.BooleanField(
        default=False
    )  
    updated_at = models.DateTimeField(
        auto_now=True
    )  

    def __str__(self):
        return self.title
