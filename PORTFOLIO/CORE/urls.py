from django.urls import include, path


urlpatterns = [
    path('', include('home.urls')),
    path('send/', include('send.urls')),
]
