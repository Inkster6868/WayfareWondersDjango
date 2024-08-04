from django.shortcuts import render
import json
from api_auth.models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from  django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.permissions import AllowAny
from rest_framework import generics


@require_POST
def login_view(request):
    data=json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    print("gsfsf", username,password)

    if not username or not password:
        return JsonResponse({"detail":"Username or password seems to be invalid"},status=403)

    user = authenticate(request, username=username, password=password)
    print("ssfsdfsdfsfsdf",user)
    if user is not None:
        login(request, user) 
        return JsonResponse({"detail": "Successfully logged in!!","data":{"username":user.username,"userId":user.id,"userEmail":user.email}}, status=200)
    else:
        return JsonResponse(
        {"detail": "Invalid Credentials!!"}, status=401
        )   


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail":"You are not logged in"})
    logout(request)
    return JsonResponse({"detail": "Successfully logged out"})

@require_POST
def register_user(request):
    try:
        data=json.loads(request.body)
        username=data.get("username","")
        email=data.get("email","")
        password=data.get("password")

        if not email or not username or not password:
            return JsonResponse({'error': 'Please fill all the required fields'}, status=400)
        User=get_user_model()
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered.'}, status=400)
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()

        return JsonResponse({'status': 'User registered successfully.'}, status=201)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"is_authenticated":False})
    return JsonResponse({"is_authenticated": True})
