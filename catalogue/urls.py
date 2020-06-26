
from django.urls import path
from .views import VendorListview, VendorDetailView

urlpatterns = [
    path('vendor/list', VendorListview.as_view(),name='catalogue-vendor-list'),
    path('vendor/detail/<int:pk>', VendorDetailView.as_view(), name='catalogue-vendor-detail')
]