from django.urls import path

from funding.views import ProductListAPI, ProductDetailAPI, FundingListAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
    path('funding/', FundingListAPI.as_view(), name='funding'),
]