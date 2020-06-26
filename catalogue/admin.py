from django.contrib import admin

# Register your models here.
from .models.vendor_model import Vendor

admin.site.register(Vendor)