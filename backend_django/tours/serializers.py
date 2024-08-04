# serializers.py
from rest_framework import serializers
from .models import Tour
from review.serializers import ReviewSerializer


class TourSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True)
    class Meta:
        model = Tour
        fields = "__all__"
