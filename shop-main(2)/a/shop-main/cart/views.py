from django.shortcuts import render,redirect
from .models import Cart
from shop.models import Product
from django.http import JsonResponse, HttpResponse
# Create your views here.
def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart



def cartView(request):
    return render(request, 'shop/cart.html')

import json
def addToCart(request):
    d = request.GET.get('data')
    data  = json.loads(d)
    print(data)
    product_id = data['product_id']
    quantity = data['count']
    cart = cart_init(request)
    cart.add(product_id,quantity)
    status = {

    }
    if cart:
        status['success'] = 200
    else:
        status['error'] = 400
    return JsonResponse(status)

def deleteCartItem(request,product_id,qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id,qty)
    return redirect('cart:cart')

def removeCart(request):
    print(request.path)
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        return redirect('cart:cart')
    cart.delete()
    return redirect('cart:cart')