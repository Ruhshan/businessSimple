from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Product, Price


class Receive(CodedBase):
    _prefix = "RECV"
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    unit = models.PositiveIntegerField(verbose_name=_("Units"))
    date = models.DateField(verbose_name=_("Receive Date"))
    price = models.ForeignKey(Price, on_delete=models.CASCADE,null=True,blank=True)
    receipt_no = models.CharField(null=True, blank=True, max_length=100, verbose_name=_("Receipt No."))

    def get_absolute_url(self):
        return reverse('operation-receive-detail', args=[self.pk])

    @property
    def get_cost(self):
        return self.price.buying * self.unit

    class Meta:
        app_label = 'operation'
        ordering = ['code']
        verbose_name = _("Receive Product")
        verbose_name_plural = _("Received Products")
        get_latest_by = "created_at"
