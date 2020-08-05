from django.urls import path
from .views import StockReportView, BalanceReportView

urlpatterns = [
    path('stock', StockReportView.as_view(), name='stock-report'),
    path('balance', BalanceReportView.as_view(), name='balance-report')

    ]