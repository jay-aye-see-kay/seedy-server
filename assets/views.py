from django.contrib.auth.models import User
from assets.models import Asset, AssetType, Brand, Location
from assets.serializers import AssetSerializer, AssetTypeSerializer, BrandSerializer, LocationSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetTypeViewSet(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
