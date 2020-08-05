from catalogue.models import Product
from operation.models import Receive, Issue, Return
from django.db.models import Sum, Subquery, OuterRef,F
from itertools import chain

def run():

    receive_value = Receive.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_receive_value=Sum(F('unit')*F('price__buying'))).values('total_receive_value')
    receive_units = Receive.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_receive_units=Sum('unit')).values('total_receive_units')

    issue_value= Issue.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_issue_value=Sum(F('unit')*F('price__selling'))).values('total_issue_value')
    issue_units = Issue.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_issue_units=Sum('unit')).values('total_issue_units')

    return_value = Return.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_return_value=Sum(F('unit')*F('price__selling'))).values('total_return_value')
    return_units = Return.objects.filter(product=OuterRef('pk')).order_by().values('product').annotate(
        total_return_units=Sum('unit')).values('total_return_units')

    Product.objects.all().annotate(total_receive_value=Subquery(receive_value),
                                         total_receive_units=Subquery(receive_units),
                                         total_issue_value=Subquery(issue_value),
                                         total_issue_units=Subquery(issue_units),
                                         total_return_value=Subquery(return_value),
                                         total_return_units=Subquery(return_units))






