from django.shortcuts import render
import json
from django.http import JsonResponse
from  django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST


@require_POST
def login_view(request):
    data=json.loads(request.body)
    print("gsfsf",data)
    return JsonResponse({"detail": "Successfully logged in!!"}, status=200)
    username=data.get("email")
    password=data.get("password")

    if not username or not password:
        return JsonResponse({"detail":"Username or password seems to be invalid"},status=403)

    user=login(username=username,password=password)
    if not user:
        return JsonResponse(
            {"detail": "Invalid Credentials!!"}, status=401
        )
    login(request,user)
    return JsonResponse({"detail":"Successfully logged in!!"},status=200)

def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail":"You are not logged in"})
    logout(request)
    return JsonResponse({"detail": "Successfully logged out"})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"is_authenticated":False})
    return JsonResponse({"is_authenticated": True})
