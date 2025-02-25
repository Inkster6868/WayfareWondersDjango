from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="api-login"),
    path("logout/", views.logout_view, name="api-logout"),
    path("register", views.register_user, name="auth-register"),
    path("session", views.session_view, name="api-session"),
]
