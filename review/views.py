from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.views.decorators.http import require_POST
from tours.models import Tour
from .models import Review

@api_view(["POST"])
def create_review(request,tour_id):
        data=(request.data)
        tour=Tour.objects.get(tour_id=tour_id)
        rating=data.get("rating")
        review_text = data.get("reviewText")
        username = data.get("username")
        Review.objects.create(tour=tour,rating=rating,review_text=review_text,username=username)
        return Response({"msg":"created"},status=status.HTTP_201_CREATED)

