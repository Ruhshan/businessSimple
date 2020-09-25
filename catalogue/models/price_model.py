from django.urls import reverse

from base.models import CodedBase
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .product_model import Product


class Price(CodedBase):
    _prefix = "PRC"
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    validFrom = models.DateField()
    validThrough = models.DateField()
    buying = models.DecimalField(default=0.0, decimal_places=2,max_digits=10)
    selling = models.DecimalField(default=0.0, decimal_places=2,max_digits=10)
    isActive = models.BooleanField(default=True)
