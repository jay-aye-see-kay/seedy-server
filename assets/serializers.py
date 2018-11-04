from rest_framework import serializers
from assets.models import Asset, AssetType, Brand, Location


class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')


class AssetSerializer(serializers.ModelSerializer):
    # location = LocationSerializer(source='id')

    class Meta:
        model = Asset
        fields = ('id', 'created', 'short_description', 'barcode',
                  'location', 'asset_type', 'brand',)
