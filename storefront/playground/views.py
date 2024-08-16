from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem



def say_hello(request):
    query_set = Product.objects.all()

    for product in query_set:
        print(product)
    
    return render(request, 'hello.html', { 'name': 'John Itopa ISAH'})

# def say_hello(request):
#     query_set = OrderItem.objects.filter(product__collection__id=3)


#     return render(request, 'hello.html', { 'name': 'John Itopa ISAH', 'products': list(query_set)})
