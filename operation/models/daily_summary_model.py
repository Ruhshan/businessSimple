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

class DailySummary(CodedBase):
    _prefix = 'SUM'
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    stockStart = models.IntegerField(default=0)
    stockEnd = models.IntegerField(default=0)
    totalReceived = models.IntegerField(default=0)
    totalIssued = models.IntegerField(default=0)
    totalReturned = models.IntegerField(default=0)
    date = models.DateField()
    objects = DailySummaryManager()

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Daily Summary")
        verbose_name_plural = _("Daily Summaries")
        get_latest_by = "date"