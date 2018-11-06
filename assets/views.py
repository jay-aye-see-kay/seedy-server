from django.contrib.auth.models import User
from assets.models import Asset, AssetType, Brand, Location
from assets.serializers import AssetSerializer, AssetTypeSerializer, BrandSerializer, LocationSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class OptionsViewSet(viewsets.ViewSet):
    def list(self, request):
        asset_types = AssetTypeSerializer(AssetType.objects.all(), many=True)
        brands = BrandSerializer(Brand.objects.all(), many=True)
        locations = LocationSerializer(Location.objects.all(), many=True)

        return Response({
            'asset_types': asset_types.data,
            'brands': brands.data,
            'locations': locations.data,
        })
