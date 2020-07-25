from django.db.models.expressions import Window, F, Subquery
from django.db.models.functions import RowNumber
from operation.models import DailySummary

def run():
    # results = DailySummary.objects.all().annotate(
    #     row_number=Window(expression=RowNumber(), partition_by=[F('product')], order_by=F('date').desc()))


    raw_query = """
        SELECT * FROM (
        SELECT *,
        ROW_NUMBER() OVER (PARTITION BY "operation_dailysummary"."product_id" ORDER BY "operation_dailysummary"."date" DESC) AS "row_number" 
        FROM "operation_dailysummary" ORDER BY "operation_dailysummary"."code" ASC) as t where t."row_number" = 1;
    """

    res = DailySummary.objects.raw(raw_query)

    for r in res:
        print(r.code,r.product.name, r.stockEnd, r.row_number)



