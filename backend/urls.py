from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("api_auth.urls")),
    path("api/v1/tours/", include("tours.urls")),
    path("api/v1/review/", include("review.urls")),
    path("api/v1/booking", include("Bookings.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
