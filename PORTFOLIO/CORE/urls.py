from django.urls import path, include


urlpatterns = [
    path("", include("home.urls")),
    path("send/", include("send.urls")),
]
