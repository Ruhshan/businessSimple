from django.urls import reverse

from base.models import CodedBase
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(CodedBase):
    _prefix = "CAT"
    name = models.CharField(verbose_name=_("Name"), max_length=127)
    remarks = models.TextField(verbose_name=_("Remarks"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse('catalogue-category-detail', args=[self.pk])

    class Meta:
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        get_latest_by = "created_at"
