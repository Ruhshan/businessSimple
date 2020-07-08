from django.db import models
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from .category_model import Category
from .vendor_model import Vendor


class Product(CodedBase):
    _prefix = "PROD"
    name = models.CharField(verbose_name=_("Name"), max_length=127)
    category = models.ForeignKey(Category, related_name="+", blank=True, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Vendor, related_name="+", blank=True, null=True, on_delete=models.SET_NULL)
    remarks = models.TextField(verbose_name=_("Remarks"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse('catalogue-product-detail', args=[self.pk])

    class Meta:
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        get_latest_by = "created_at"
