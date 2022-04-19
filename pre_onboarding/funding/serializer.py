from rest_framework import serializers

from funding.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'seller', 'desc', 'goal', 'end_date', 'charge', 'created_at')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'seller', 'desc', 'goal', 'end_date', 'charge', 'created_at')
        read_only_fields = ('goal',)  # 목표 금액은 변경 불가
