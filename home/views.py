from django.shortcuts import render, redirect
from .models import StockMarket
from .forms import DataForm
from django.core.paginator import Paginator, EmptyPage
from .filters import DataFilter

# Function to load data from model StockMarket
def homePage(request):
    data = StockMarket.objects.all()
    # p = Paginator(data,100)
    # page_num = request.GET.get('page',1)

    # try:
    #     page = p.page(page_num)
    # except EmptyPage:
    #     page = p.page(1)

    myFilter = DataFilter(request.GET,queryset=data)
    data = myFilter.qs

    context = {
        'data': data,
        'filter': myFilter,
    }
    return render(request, 'home/home_page.html', context)

# Adds new data to the database.
def addData(request):
    if request.method == 'POST':
        form = DataForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DataForm()
    return render(request, 'home/add_data.html', {'form':form})


#Updates the data of the database
def updateData(request, pk):
    data = StockMarket.objects.get(id=pk)
    form = DataForm(instance=data)

    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')

    value = {'form':form}
    return render(request, 'home/add_data.html', value)


#Deletes a particular data
def deleteData(request, pk):
    data = StockMarket.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return redirect('/')

    value = {'item':data}
    return render(request, 'home/delete_data.html', value)


