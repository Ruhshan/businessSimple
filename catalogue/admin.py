from django.contrib import admin

# Register your models here.
from .models.vendor_model import Vendor
from .models.price_model import Price
from .models.unit_name_model import UnitName

admin.site.register(Vendor)
admin.site.register(Price)
admin.site.register(UnitName)