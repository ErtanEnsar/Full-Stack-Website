from django.db import models

# Create your models here.
class Stock(models.Model):
    Name = models.CharField(max_length=45)
    Ticker = models.CharField(max_length=20)
    Exchange = models.CharField(max_length=150)
    Sentiment_Today = models.IntegerField(blank=True, null=True)
    Mentions_Today = models.IntegerField(blank=True, null=True)