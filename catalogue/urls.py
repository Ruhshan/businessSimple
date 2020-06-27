
from django.urls import path
from .views import VendorListview, VendorDetailView, VendorCreateView, VendorUpdateView
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView

urlpatterns = [
    path('vendor/list', VendorListview.as_view(),name='catalogue-vendor-list'),
    path('vendor/detail/<int:pk>', VendorDetailView.as_view(), name='catalogue-vendor-detail'),
    path('vendor/create',VendorCreateView.as_view(), name='catalogue-vendor-create'),
    path('vendor/update/<int:pk>', VendorUpdateView.as_view(), name='catalogue-vendor-update'),
    path('category/list', CategoryListView.as_view(), name="catalogue-category-list"),
    path('category/create', CategoryCreateView.as_view(), name='catalogue-category-create'),
    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='catalogue-category-detail'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='catalogue-category-update')
]