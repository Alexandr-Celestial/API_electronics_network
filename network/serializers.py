from rest_framework import serializers

from network.models import Product, NetworkLink


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product"""
    class Meta:
        model = Product
        fields = "__all__"


class NetworkLinkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели NetworkLink"""

    products = ProductSerializer(many=True, read_only=True)
    arrears = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = NetworkLink
        fields = "__all__"
