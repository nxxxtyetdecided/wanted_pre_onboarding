from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from funding.models import Product, Funding
from funding.serializer import ProductListSerializer, ProductCreateSerializer, \
    ProductDetailSerializer, FundingListSerializer


# 상품 목록 및 생성
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ('title',)
    ordering_fields = ('created_at', 'total')

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = ProductCreateSerializer
        return serializer_class


# 상품 디테일, 수정, 삭제
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# 상품 목록 및 생성
class FundingListAPI(generics.ListCreateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingListSerializer

    def post(self, request, *args, **kwargs):
        target_product = self.request.data['product']
        product = Product.objects.filter(pk=target_product).get()
        product.total += product.charge
        product.cnt += 1
        product.save()
        return self.create(request, *args, **kwargs)
