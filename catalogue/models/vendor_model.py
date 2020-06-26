from django.db import models

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _


class Vendor(CodedBase):
    _prefix = "VENDOR"
    name = models.CharField(verbose_name=_("Name"), max_length=127)
    address = models.TextField(verbose_name=_("Address"), blank=True, null=True)
    phone = models.CharField(verbose_name=_("Phone"), blank=True, null=True, max_length=127)
    email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    remarks = models.TextField(verbose_name=_("Remarks"), blank=True, null=True)

    class Meta:
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")
        get_latest_by = "created_at"
