from django.db import models
from django.db.models import Sum, F, OuterRef, Subquery, DecimalField
from django.urls import reverse

from base.models import CodedBase
from django.utils.translation import ugettext_lazy as _
from django.apps import apps

from .category_model import Category
from .vendor_model import Vendor
from .unit_name_model import UnitName


class ProductManager(models.Manager):
    def get_balance_report(self,startDate, endDate):
        receive_model = apps.get_model('operation.receive')
        issue_model = apps.get_model('operation.issue')
        return_model = apps.get_model('operation.return')

        receive_value = receive_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_receive_value=Sum(F('unit') * F('price__buying'),output_field=DecimalField())).values('total_receive_value')
        receive_units = receive_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_receive_units=Sum('unit')).values('total_receive_units')
        receive_bonus = receive_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_receive_bonus=Sum(F('bonusUnits') )).values('total_receive_bonus')

        issue_value = issue_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_issue_value=Sum(F('unit') * F('price__selling'),output_field=DecimalField())).values('total_issue_value')
        issue_units = issue_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_issue_units=Sum('unit')).values('total_issue_units')
        issue_bonus = issue_model.objects.filter(product=OuterRef('pk'),
                                                 date__range=[startDate, endDate]).order_by().values('product').annotate(
            total_issue_bonus=Sum('bonusUnits')).values('total_issue_bonus')

        return_value = return_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_return_value=Sum(F('unit') * F('price__selling'),output_field=DecimalField())).values('total_return_value')
        return_units = return_model.objects.filter(product=OuterRef('pk'),date__range=[startDate,endDate]).order_by().values('product').annotate(
            total_return_units=Sum('unit')).values('total_return_units')

        return self.all().annotate(total_receive_value=Subquery(receive_value),
                                       total_receive_units=Subquery(receive_units),
                                       total_issue_value=Subquery(issue_value),
                                       total_receive_bonus=Subquery(receive_bonus),
                                       total_issue_units=Subquery(issue_units),
                                       total_return_value=Subquery(return_value),
                                       total_issue_bonus=Subquery(issue_bonus),
                                       total_return_units=Subquery(return_units))

class Product(CodedBase):
    _prefix = "PROD"
    name = models.CharField(verbose_name=_("Name"), max_length=127)
    category = models.ForeignKey(Category, related_name="+", blank=True, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Vendor, related_name="+", blank=True, null=True, on_delete=models.SET_NULL)
    remarks = models.TextField(verbose_name=_("Remarks"), blank=True, null=True)
    unitName = models.ForeignKey(UnitName, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Unit Name"))
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('catalogue-product-detail', args=[self.pk])

    class Meta:
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        get_latest_by = "created_at"
