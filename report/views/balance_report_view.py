from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from report.forms import BalanceReportForm
from django.shortcuts import render
from catalogue.models import Product


class BalanceReportView(LoginRequiredMixin,View):
    def get(self,request):
        form = BalanceReportForm()
        return render(request,'report/balance_report.html',{'form':form})

    def post(self, request):
        form = BalanceReportForm(request.POST)
        balances = Product.objects.get_balance_report()
        return render(request, 'report/balance_report.html', {'form': form,'balances':balances})