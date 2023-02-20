import datetime, json
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import template
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.authentication.models import User
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from collections import OrderedDict
from django.utils.safestring import mark_safe
from apps.store.models import Product
from .cart import Cart
from .models import Discount
from decimal import Decimal


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_carts_product_count(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        counter = len(cart)
        print("counter", counter)
        context['data'] = counter if counter > 0 else ''
        return JsonResponse(context, status=200)
    return JsonResponse(context, status=400)


def add_remove_product(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        product_id = request.GET.get("product_id", None)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        counter = len(cart)
        context['counter'] = counter if counter > 0 else ''
        context['total'] = cart.get_total_price()
        return JsonResponse(context, status=200)
    return JsonResponse(context, status=400)


def add_product_to_cart(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        # todo if user logged add product to datatable
        cart = Cart(request)
        product_id = request.GET.get("product_id", None)
        quantity = request.GET.get("quantity", 1)
        update = request.GET.get("update", False)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity,
                 update_quantity=update)
        counter = len(cart)
        context['counter'] = counter if counter > 0 else ''
        context['total'] = cart.get_total_price()
        context['product_name'] = product.name
        return JsonResponse(context, status=200)
    return JsonResponse({}, status=400)


def get_discount(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        context['total_discount'] = cart.get_total_price_discount()
        return JsonResponse(context, status=200)
    return JsonResponse({}, status=400)


def add_discount(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        discount_name = request.GET.get("discount_name", "")
        discount = Discount.objects.get(name=discount_name)
        request.session['discount'] = {"discount_name": discount.name, "discount_percentage": float(Decimal(discount.percentage))}

        context['discount_name'] = discount.name
        context['discount_percentage'] = discount.percentage
        context['total'] = cart.get_total_price()
        return JsonResponse(context, status=200)
    return JsonResponse({}, status=400)


class CartSubtotal(View):

    def get(self, request):
        context = {}
        # cart_products = request.session.get('cart_products', {})
        # products_temp = []
        # for key, val in cart_products.items():
        #     product = Product.objects.get(name=key)
        #     product.quantity = val
        #     products_temp.append(product)
        cart = Cart(request)
        # print("====",[item for item in cart])
        discount = request.session.get('discount', {'discount_name': "", 'discount_percentage': 0})
        # print("CART", discount['discount_name'])
        context['cart'] = cart
        context['total'] = cart.get_total_price()
        context['total_discount'] = cart.get_total_price_discount()
        context['discount_name'] = discount['discount_name']
        context['discount_percentage'] = int(discount['discount_percentage'])
        return render(request, 'cart/cart-subtotal.html', context)

    def post(self, request):
        pass


class CartCheckout(View):

    def get(self, request):
        context = {}
        context['n'] = range(100, 900, 100)
        return render(request, 'cart/cart-checkout.html', context)

    def post(self, request):
        pass

