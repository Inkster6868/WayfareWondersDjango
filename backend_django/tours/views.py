# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour
from .serializers import TourSerializer


@api_view(["POST"])
def create_tour(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Successfully created",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {"success": False, "message": "Failed to create, Try again."},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["PUT"])
def update_tour(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response(
            {"success": False, "message": "Tour not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = TourSerializer(tour, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Successfully updated",
                "data": serializer.data,
            }
        )
    return Response(
        {"success": False, "message": "Failed to update"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["DELETE"])
def delete_tour(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response(
            {"success": False, "message": "Tour not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    tour.delete()
    return Response(
        {"success": True, "message": "Successfully deleted"},
        status=status.HTTP_204_NO_CONTENT,
    )


@api_view(["GET"])
def get_single_tour(request, id):
    try:
        tour = Tour.objects.get(tour_id=id)
    except Tour.DoesNotExist:
        return Response(
            {"success": False, "message": "Tour does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = TourSerializer(tour)
    return Response({"success": True, "message": "Fetched", "data": serializer.data})


@api_view(["GET"])
def get_all_tour(request):
    page = int(request.GET.get("page", 0))
    limit = 8
    tours = Tour.objects.all()[page * limit : (page + 1) * limit]
    serializer = TourSerializer(tours, many=True)
    return Response(
        {
            "success": True,
            "count": len(serializer.data),
            "message": "Fetched all",
            "data": serializer.data,
        }
    )


@api_view(["GET"])
def get_tour_by_search(request):
    city = request.GET.get("city", "")
    distance = int(request.GET.get("distance", 0))
    max_group_size = int(request.GET.get("maxGroupSize", 0))

    tours = Tour.objects.filter(
        city__icontains=city, distance__gte=distance, max_group_size__gte=max_group_size
    )
    serializer = TourSerializer(tours, many=True)
    return Response({"success": True, "message": "Fetched", "data": serializer.data})


@api_view(["GET"])
def get_featured_tour(request):
    tours = Tour.objects.filter(featured=True)[:8]
    serializer = TourSerializer(tours, many=True)
    return Response(
        {"success": True, "message": "Fetched featured", "data": serializer.data}
    )


@api_view(["GET"])
def get_tour_count(request):
    count = Tour.objects.count()
    return Response({"success": True, "data": count})

