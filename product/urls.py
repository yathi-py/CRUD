from django.urls import path
from .views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>/details', ProductDetailView.as_view(), name='product_detail'),
    path('create', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete')
]
