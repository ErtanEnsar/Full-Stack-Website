from django.contrib import admin

# Register your models here.
from .models import Stock
from .models import StockData
admin.site.register(Stock)
admin.site.register(StockData)
