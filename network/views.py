from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from network.models import NetworkLink, Product
from network.serializers import NetworkLinkSerializer, ProductSerializer


class IsActiveEmployee(permissions.BasePermission):
    """Предоставляет доступ только активным сотрудникам"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active

class NetworkLinkViewSet(viewsets. ModelViewSet):
    """CRUD для модели NetworkLink с возможностью фильтрации по стране"""
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]

class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для модели Product с возможностью фильтрации по стране"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    

