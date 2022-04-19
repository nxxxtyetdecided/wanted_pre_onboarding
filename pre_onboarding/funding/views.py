from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from funding.models import Product
from funding.serializer import ProductListSerializer, ProductDetailSerializer


# 상품 목록 및 생성
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ('title',)
    ordering_fields = ('created_at',)


# 상품 디테일, 수정, 삭제
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
