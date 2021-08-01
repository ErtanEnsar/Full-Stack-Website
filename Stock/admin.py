from django.contrib import admin

# Register your models here.
from .models import Stock
from .models import Date
admin.site.register(Stock,Date)
