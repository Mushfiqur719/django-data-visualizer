from django.contrib import admin
from .models import StockMarket

from import_export.admin import ImportExportModelAdmin



class ViewAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('date','trade_code','high','low','open','close','volume')
    list_filter = ['trade_code']

admin.site.register(StockMarket,ViewAdmin)