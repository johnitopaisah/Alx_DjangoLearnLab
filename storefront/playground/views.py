from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem



def say_hello(request):
    
    # query_set = Product.objects.filter(inventory__lt=10)
    query_set = Product.objects.order_by('unit_price', '-title').reverse()
    
    return render(request, 'hello.html', { 'name': 'John Itopa ISAH', 'products': list(query_set)})

# def say_hello(request):
#     query_set = OrderItem.objects.filter(product__collection__id=3)


#     return render(request, 'hello.html', { 'name': 'John Itopa ISAH', 'products': list(query_set)})
