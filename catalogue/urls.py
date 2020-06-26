
from django.urls import path
from .views import VendorListview

urlpatterns = [
    path('vendor/list', VendorListview.as_view(),name='catalogue-vendor-list')
]