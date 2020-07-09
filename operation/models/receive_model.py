from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product


class Receive(CodedBase):
    _prefix = "RECV"
    product = models.ForeignKey(Product, related_name="+", on_delete=models.DO_NOTHING)
    unit = models.IntegerField(verbose_name=_("Units"))
    date = models.DateField(verbose_name=_("Receive Date"))
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Receive Product")
        verbose_name_plural = _("Received Products")
        get_latest_by = "created_at"
