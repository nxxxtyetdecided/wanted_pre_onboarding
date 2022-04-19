from django.urls import path

from funding.views import ProductListAPI, ProductDetailAPI

urlpatterns = [
    path('', ProductListAPI.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
]