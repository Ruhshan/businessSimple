from catalogue.models import Product
from operation.models import Receive, Issue, Return
from django.db.models import Sum, Subquery, OuterRef
from itertools import chain

def run():

    receives_q = Receive.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_receive=Sum('unit')).values('total_receive')
    issues_q = Issue.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_issues=Sum('unit')).values('total_issues')

    returns_q = Return.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_returns=Sum('unit')).values('total_returns')

    prc = Product.objects.all().annotate(total_receives=Subquery(receives_q),
                                         total_issues=Subquery(issues_q),
                                         total_returns=Subquery(returns_q))


    for p in prc:
        print(p.name, p.total_receives, p.total_issues,p.total_returns)



