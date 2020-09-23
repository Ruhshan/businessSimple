from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from report.forms import BalanceReportForm
from django.shortcuts import render
from catalogue.models import Product
from datetime import date


class BalanceReportView(LoginRequiredMixin,View):
    def get(self,request):
        today, fistOfMonth = self._getDefaultDateRange()

        form = BalanceReportForm(initial={'startDate':str(fistOfMonth),'endDate':str(today)})
        balances = Product.objects.get_balance_report(fistOfMonth, today)
        return render(request,'report/balance_report.html',{'form':form,'balances':balances})

    def post(self, request):
        form = BalanceReportForm(request.POST)
        if form.is_valid():
            balances = Product.objects.get_balance_report(form.cleaned_data['startDate'], form.cleaned_data['endDate'])
            return render(request, 'report/balance_report.html', {'form': form,'balances':balances})
        return render(request, 'report/balance_report.html', {'form': form})

    def _getDefaultDateRange(self):
        today = date.today()
        firstOfMonth = today.replace(day=1)
        return (today, firstOfMonth)