from django.db import models

class StockMarket(models.Model):

    date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    trade_code = models.CharField(max_length=20)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    open = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.IntegerField(null=True)

    def __str__(self):
        return f'Date : {self.date} - Code: {self.trade_code}'

