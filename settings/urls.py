from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from settings import base

urlpatterns = [
    path("list_municipality_ajax/", base.list_municipality_ajax,  name="list_municipality_ajax"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

