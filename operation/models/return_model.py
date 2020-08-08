from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product, Price


class Return(CodedBase):
    _prefix = "RET"
    product = models.ForeignKey(Product, related_name="+", on_delete=models.DO_NOTHING)
    unit = models.PositiveIntegerField(verbose_name=_("Units"))
    price = models.ForeignKey(Price, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(verbose_name=_("Return Date"))
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))
    customer = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Customer Name"))
    remarks = models.TextField(null=True, blank=True, verbose_name=_("Remarks"))

    def get_absolute_url(self):
        return reverse('operation-return-detail', args=[self.pk])

    @property
    def get_cost(self):
        return self.unit*self.price.selling

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Returned Product")
        verbose_name_plural = _("Returned Products")
        get_latest_by = "date"