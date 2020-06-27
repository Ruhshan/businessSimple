from base.models import CodedBase
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(CodedBase):
    _prefix = "CAT"
    name = models.CharField(verbose_name=_("Name"), max_length=127)

    class Meta:
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        get_latest_by = "created_at"
