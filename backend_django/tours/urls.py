# urls.py
from django.urls import path
from .views import (
    create_tour,
    update_tour,
    delete_tour,
    get_single_tour,
    get_all_tour,
    get_tour_by_search,
    get_featured_tour,
    get_tour_count,
)

urlpatterns = [
    path("tours/", get_all_tour, name="get_all_tour"),
    path("<str:id>/", get_single_tour, name="get_single_tour"),
    path("tours/create/", create_tour, name="create_tour"),
    path("tours/<int:id>/update/", update_tour, name="update_tour"),
    path("tours/<int:id>/delete/", delete_tour, name="delete_tour"),
    path("search/getTourBySearch", get_tour_by_search, name="get_tour_by_search"),
    path("search/getFeaturedTours", get_featured_tour, name="get_featured_tours"),
    path("tours/count/", get_tour_count, name="get_tour_count"),
]
