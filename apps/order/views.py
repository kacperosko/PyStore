import datetime
import json
from collections import OrderedDict
from decimal import Decimal
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist

from apps.authentication.models import User, Address, Unregistered_User
from apps.store.models import Product
from .cart import Cart
from .forms import CartCheckoutForm
from .models import Discount, Order, Order_Item


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_carts_product_count(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        counter = len(cart)
        context['data'] = counter if counter > 0 else ''
        return JsonResponse(context, status=200)
    return JsonResponse(context, status=400)


def remove_product(request):
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
        update = str(request.GET.get("update", "false"))
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
    status = 400
    if is_ajax(request) and request.method == "GET":
        cart = Cart(request)
        discount_name = request.GET.get("discount_name", "")
        try:
            discount = Discount.objects.get(name=discount_name)
            context['discount_name'] = discount.name
            context['discount_percentage'] = discount.percentage
            context['total'] = cart.get_total_price()
            if 'discount' not in request.session:
                request.session['discount'] = {"discount_name": discount.name,
                                               "discount_percentage": float(Decimal(discount.percentage))}
                status = 200
            else:
                print(401)
                status = 401
                context['message'] = 'Discount \"' + discount_name + '\" is already added ;)'
        except Discount.DoesNotExist:
            context['message'] = 'Discount \"' + discount_name + '\" wasn\'t found'
            print(context['message'])
            status = 402

        return JsonResponse(context, status=status)
    status = 400
    return JsonResponse({}, status=status)


class CartSubtotal(View):

    @staticmethod
    def get(request):
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

    @staticmethod
    def get(request):
        context = {}

        return render(request, 'cart/cart-checkout.html', context)

    @staticmethod
    def post(request):
        print(request.POST)
        print(request.GET.get("discount_name", ""))
        form = CartCheckoutForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            address = Address.objects.create(address=form.cleaned_data['address'], city=form.cleaned_data['city'],
                                             country=form.cleaned_data['country'],
                                             postal_code=form.cleaned_data['postal_code'], )
            user, unregistered_user = None, None
            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)
                user.address = address
                user.save()
            else:
                unregistered_user = Unregistered_User.objects.create(email=form.cleaned_data['email'],
                                                                     first_name=form.cleaned_data['first_name'],
                                                                     last_name=form.cleaned_data['last_name'],
                                                                     address=address)
            try:
                discount = Discount.objects.get(
                    name=request.session.get('discount', {'discount_name': ""})['discount_name'])
            except ObjectDoesNotExist:
                discount = None

            order = Order.objects.create(user=user,
                                         unregistered_user=unregistered_user,
                                         discount=discount
                                         )

            for item in cart:
                Order_Item.objects.create(order=order,
                                          quantity=item['quantity'],
                                          price=item['price'],
                                          product=item['product']
                                          )

            return render(request, 'cart/submitted.html', {'message': "SUCCESS"})
        else:
            return render(request, 'cart/submitted.html', {'message': 'ERROR'})
