from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product, Price


class Issue(CodedBase):
    _prefix = "ISSU"
    product = models.ForeignKey(Product, related_name="+", on_delete=models.DO_NOTHING)
    unit = models.PositiveIntegerField(verbose_name=_("Units"))
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_("Issue Date"))
    bonusUnits = models.PositiveIntegerField(default=0, verbose_name=_("Issued Bonus Units"))
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))
    customer = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Customer Name"))
    remarks = models.TextField(default="", verbose_name=_("Remarks"))
    
    def get_absolute_url(self):
        return reverse('operation-issue-detail', args=[self.pk])

    def get_cost(self):
        return self.unit * self.price.selling

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Issue Product")
        verbose_name_plural = _("Issue Products")
        get_latest_by = "date"
