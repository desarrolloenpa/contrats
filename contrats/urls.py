from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("contracts.urls")),
    path("settings/", include("settings.urls")),
    path("contracts/", include("contracts.urls")),
]
