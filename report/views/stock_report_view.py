from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View
from operation.models import DailySummary
from report.forms import StockReportForm

class StockReportView(LoginRequiredMixin,View):
    def get(self, request):
        form = StockReportForm()
        todays_stock = DailySummary.objects.get_stock_for_today()
        return render(request, 'report/stock_report.html',{'form':form,'stocks':todays_stock})

    def post(self, request):
        form = StockReportForm(request.POST)

        if form.is_valid():
            todays_stock = DailySummary.objects.get_stock_for_date(form.cleaned_data.get('date'))
            return render(request, 'report/stock_report.html', {'form': form, 'stocks': todays_stock})

        return render(request, 'report/stock_report.html', {'form': form})


