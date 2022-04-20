from rest_framework import serializers

from funding.models import Product, Funding


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'seller',
            'desc',
            'end_date',
            'charge',
            'goal',
        )


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'seller',
            'd_day',
            'total',
            'achievement',
        )

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'seller',
            'desc',
            'goal',
            'd_day',
            'charge',
            'total',
            'cnt',
            'achievement',
        )
        read_only_fields = ('goal',)  # 목표 금액은 변경 불가


class FundingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ('customer', 'product')
