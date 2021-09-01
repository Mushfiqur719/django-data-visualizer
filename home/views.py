import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# Create your views here.

with open('stock_market_data.json') as d:
    data = json.load(d)


def home_page(request):
    return render(request,'home/home_page.html',{'data': data})