from django.urls import path, include

from network.apps import NetworkConfig
from rest_framework.routers import DefaultRouter

from network.views import NetworkLinkViewSet, ProductViewSet

app_name =NetworkConfig.name

router = DefaultRouter()
router.register(r"networklinks", NetworkLinkViewSet, basename="networklink")
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
] + router.urls