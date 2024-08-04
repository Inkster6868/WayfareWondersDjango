from django.urls import path
from .views import create_review

urlpatterns= [
    path("<str:tour_id>",create_review,name="create-review"),
]