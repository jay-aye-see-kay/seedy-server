from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class AssetType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=20, blank=True, default='')
    barcode = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        default='',
    )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )
    asset_type = models.ForeignKey(
        AssetType,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )
    brand = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )

    def __str__(self):
        if (self.short_description):
            return self.short_description
        if (self.barcode):
            return self.barcode

        return "Unnamed tool"
