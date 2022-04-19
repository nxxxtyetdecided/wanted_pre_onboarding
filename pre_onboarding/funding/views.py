from rest_framework import generics

from funding.models import Product
from funding.serializer import ProductListSerializer, ProductDetailSerializer


# 상품 목록 및 생성
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


# 상품 디테일, 수정, 삭제
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
