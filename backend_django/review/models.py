from django.db import models
from tours.models import Tour
import uuid


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True)
    tour = models.ForeignKey(
        Tour, related_name="reviews", on_delete=models.CASCADE
    )  
    username = models.CharField(
        max_length=255
    ) 
    review_text = models.TextField()  
    rating = models.PositiveIntegerField()  
    created_at = models.DateTimeField(
        auto_now_add=True
    )  
    updated_at = models.DateTimeField(
        auto_now=True
    ) 
