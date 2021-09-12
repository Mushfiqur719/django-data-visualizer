import django_filters
from .models import StockMarket

class DataFilter(django_filters.FilterSet):
    class Meta:
        model = StockMarket
        fields = ['trade_code']
