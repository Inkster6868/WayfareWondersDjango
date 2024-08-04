from django.urls import path, include
from .views import create_booking

urlpatterns=[
    path("/",create_booking,name="create-booking")
]