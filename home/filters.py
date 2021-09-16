import django_filters
from .models import StockMarket

class DataFilter(django_filters.FilterSet):
    # trade_code = django_filters.ModelChoiceFilter(queryset=StockMarket.objects.filter(trade_code='trade_code'),label='Select Trade Code')
    class Meta:
        model = StockMarket
        fields = ['trade_code']
