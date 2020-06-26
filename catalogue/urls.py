
from django.urls import path
from .views import VendorListview, VendorDetailView, VendorCreateView, VendorUpdateView

urlpatterns = [
    path('vendor/list', VendorListview.as_view(),name='catalogue-vendor-list'),
    path('vendor/detail/<int:pk>', VendorDetailView.as_view(), name='catalogue-vendor-detail'),
    path('vendor/create',VendorCreateView.as_view(), name='catalogue-vendor-create'),
    path('vendor/update/<int:pk>', VendorUpdateView.as_view(), name='catalogue-vendor-update')
]