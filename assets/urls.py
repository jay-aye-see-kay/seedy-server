from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assets import views

router = DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'options', views.OptionsViewSet, basename='options')
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
