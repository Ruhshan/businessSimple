from django.urls import path
from .views import StockReportView

urlpatterns = [
    path('stock', StockReportView.as_view(), name='stock-report')
    ]