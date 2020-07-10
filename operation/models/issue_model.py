from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product


class Issue(CodedBase):
    _prefix = "ISSU"
    product = models.ForeignKey(Product, related_name="+", on_delete=models.DO_NOTHING)
    unit = models.IntegerField(verbose_name=_("Units"))
    date = models.DateField(verbose_name=_("Issue Date"))
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))
    customer = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Customer Name"))

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Issue Product")
        verbose_name_plural = _("Issue Products")
        get_latest_by = "date"
