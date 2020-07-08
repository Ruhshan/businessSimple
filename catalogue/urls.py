
from django.urls import path
from .views import VendorListview, VendorDetailView, VendorCreateView, VendorUpdateView
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView
from .views import ProductCreateView, ProductDetailView, ProductListView, ProductUpdateView

urlpatterns = [
    path('vendor/list', VendorListview.as_view(),name='catalogue-vendor-list'),
    path('vendor/detail/<int:pk>', VendorDetailView.as_view(), name='catalogue-vendor-detail'),
    path('vendor/create',VendorCreateView.as_view(), name='catalogue-vendor-create'),
    path('vendor/update/<int:pk>', VendorUpdateView.as_view(), name='catalogue-vendor-update'),
    path('category/list', CategoryListView.as_view(), name="catalogue-category-list"),
    path('category/create', CategoryCreateView.as_view(), name='catalogue-category-create'),
    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='catalogue-category-detail'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='catalogue-category-update'),
    path('product/list', ProductListView.as_view(), name="catalogue-product-list"),
    path('product/create', ProductCreateView.as_view(), name='catalogue-product-create'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name='catalogue-product-detail'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='catalogue-product-update')
]