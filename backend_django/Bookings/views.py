from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bookings
from api_auth.models import User


from rest_framework import status


@api_view(["POST"])
def create_booking(request):
    data = request.data
    user_id = User.objects.get(id=data.get("userId"))
    userEmail = data.get("userEmail")
    tourName = data.get("tourName")
    fullName = data.get("fullName")
    guestSize = data.get("guestSize")
    phone = data.get("phone")
    Bookings.objects.create(user_id=user_id,userEmail=userEmail,tourName=tourName,fullName=fullName,guestSize=guestSize,phone=phone)
    return Response({"msg":"created"},status=status.HTTP_201_CREATED)
