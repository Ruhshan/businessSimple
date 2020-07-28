from catalogue.models import Product
from operation.models import Receive, Issue
from django.db.models import Sum
from itertools import chain

def run():
    rec = Receive.objects.all().values('product__id').order_by('product__name').annotate(rec_sum=Sum('unit'))
    iss = Issue.objects.all().values('product__id').order_by('product__name').annotate(iss_sum=Sum('unit'))

    for r in rec:
        print(r)
