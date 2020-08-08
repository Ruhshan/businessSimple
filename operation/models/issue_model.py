from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product, Price


class Issue(CodedBase):
    _prefix = "ISSU"
    product = models.ForeignKey(Product, related_name="+", on_delete=models.DO_NOTHING)
    unit = models.PositiveIntegerField(verbose_name=_("Units"))
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateField(verbose_name=_("Issue Date"))
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))
    customer = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Customer Name"))
    
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
