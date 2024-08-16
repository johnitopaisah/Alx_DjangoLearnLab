from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem



def say_hello(request):
    
    query_set = Product.objects.filter(description__isnull=True)
    
    return render(request, 'hello.html', { 'name': 'John Itopa ISAH', 'products': list(query_set)})

# def say_hello(request):
#     query_set = OrderItem.objects.filter(product__collection__id=3)


#     return render(request, 'hello.html', { 'name': 'John Itopa ISAH', 'products': list(query_set)})
