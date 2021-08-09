from django.urls import path, include
from rest_framework import routers

from categories.views import ListProductsAPIView, CreateProductsAPIView, UpdateProductsAPIView, DeleteProductsAPIView, ListCategoryAPIView, CreateCategoryAPIView

app_name = 'Categories'

# router = routers.DefaultRouter()
# router.register(r'products',ProductViewSet)


urlpatterns = [
    path("products/",ListProductsAPIView.as_view(),name="list_products"),
    path("products/create/", CreateProductsAPIView.as_view(),name="create_products"),
    path("products/update/<int:pk>/",UpdateProductsAPIView.as_view(),name="update_products"),
    path("products/delete/<int:pk>/",DeleteProductsAPIView.as_view(),name="delete_products"),
    
    path("category/",ListCategoryAPIView.as_view(),name="list_categories"),
    path("category/create/", CreateCategoryAPIView.as_view(),name="create_category"),

]
