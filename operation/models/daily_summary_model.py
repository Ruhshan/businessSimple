from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product


class DailySummaryManager(models.Manager):
    def has_previous_summary(self, product, form_date):
        return self.filter(product=product, date__lte=form_date).exists()

    def get_summary_for_date(self, product, form_date):
        obj, created = self.get_or_create(product=product,date=form_date)

        if created:
            last_summary = self.filter(product=product, date__lt=form_date).order_by('date').last()
            obj.stockStart = last_summary.stockEnd
            obj.stockEnd = last_summary.stockEnd
            obj.save()
        return obj

    def get_summary_after_date(self, product, form_date):
        return self.filter(product=product, date__gte=form_date).order_by('date')

    def get_stock_for_today(self):
        raw_query = """
                SELECT * FROM (
                SELECT *,
                ROW_NUMBER() OVER (PARTITION BY "operation_dailysummary"."product_id" ORDER BY "operation_dailysummary"."date" DESC) AS "row_number" 
                FROM "operation_dailysummary" ORDER BY "operation_dailysummary"."code" ASC) as t where t."row_number" = 1;
            """
        return self.raw(raw_query)

    def get_stock_for_date(self,date, product=None):
        raw_query = """
                        SELECT * FROM (
                        SELECT *,
                        ROW_NUMBER() OVER (PARTITION BY "operation_dailysummary"."product_id" ORDER BY "operation_dailysummary"."date" DESC) AS "row_number" 
                        FROM "operation_dailysummary" WHERE "operation_dailysummary"."date"<= '{date}' and "operation_dailysummary"."product_id" {pv} ORDER BY "operation_dailysummary"."code" ASC) as t where t."row_number" = 1;
                    """.format(date=date.strftime("%Y-%m-%d"), pv="= "+str(product.id) if product is not None else 'is not null')

        return self.raw(raw_query)


class DailySummary(CodedBase):
    _prefix = 'SUM'
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    stockStart = models.IntegerField(default=0)
    stockEnd = models.IntegerField(default=0)
    totalReceived = models.IntegerField(default=0)
    totalIssued = models.IntegerField(default=0)
    totalReturned = models.IntegerField(default=0)
    bonusReceived = models.IntegerField(default=0)
    bonusIssued = models.IntegerField(default=0)
    date = models.DateField()
    objects = DailySummaryManager()

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Daily Summary")
        verbose_name_plural = _("Daily Summaries")
        get_latest_by = "date"