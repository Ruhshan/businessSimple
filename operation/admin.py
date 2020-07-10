from django.contrib import admin

from operation.models import DailySummary

class DailySummaryAdmin(admin.ModelAdmin):
    list_display = ['code', 'date','stockStart','stockEnd','totalReceived']

admin.site.register(DailySummary, DailySummaryAdmin)
# Register your models here.
