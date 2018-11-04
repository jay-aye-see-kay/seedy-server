from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('assets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
