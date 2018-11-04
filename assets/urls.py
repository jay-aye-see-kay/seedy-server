from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assets import views

router = DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'assettypes', views.AssetTypeViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'locations', views.LocationViewSet)
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
