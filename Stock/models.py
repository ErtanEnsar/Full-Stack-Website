from django.db import models
from datetime import date


# Create your models here.
class Date(models.Model):
    Date_Today = models.DateField(default=date.today)
    Sentiment_Today = models.IntegerField(blank=True, null=True)
    Mentions_Today = models.IntegerField(blank=True, null=True)


class Stock(models.Model):
    Name = models.CharField(max_length=45)
    Ticker = models.CharField(max_length=20)
    Exchange = models.CharField(max_length=150)
    Todays_Date_For_Stock = models.ForeignKey(Date, on_delete=models.PROTECT)

