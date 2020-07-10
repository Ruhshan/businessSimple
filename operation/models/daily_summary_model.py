from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product


class DailySummary(CodedBase):
    _prefix = 'SUM'
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    stockStart = models.IntegerField()
    stockEnd = models.IntegerField()
    totalReceived = models.IntegerField()
    totalIssued = models.IntegerField()
    totalReturned = models.IntegerField()

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Daily Summary")
        verbose_name_plural = _("Daily Summaries")
        get_latest_by = "date"