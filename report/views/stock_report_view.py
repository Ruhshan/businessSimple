from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View
from operation.models import DailySummary
from report.forms import StockReportForm

class StockReportView(LoginRequiredMixin,View):
    def get(self, request):
        form = StockReportForm()
        return render(request, 'report/stock_report.html',{'form':form})


