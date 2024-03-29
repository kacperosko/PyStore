import datetime, json
from django.shortcuts import redirect, render
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
from .models import Product, Product_Attribute, Attribute
from django.contrib.auth.mixins import LoginRequiredMixin


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def about_us(request):
    return render(request, 'store/about-us.html', {})


def blog(request):
    return render(request, 'blog/blog-home.html', {})


def set_theme(request):
    if is_ajax(request) and request.method == "GET":
        try:
            color_theme = request.GET.get("color_theme", "")
            request.session['discount'] = color_theme
            status = 200
        except Exception as e:
            status = 400
        return JsonResponse({}, status=status)
    status = 400
    return JsonResponse({}, status=status)


def get_product(request, product_url):
    content = {}
    try:
        content['product'] = Product.objects.get(url=product_url)
    except ObjectDoesNotExist:
        return render(request, 'store/index.html', content)

    return render(request, 'store/product.html', content)


def home_page(request):
    content = {}
    p = Product.objects.get(name="Monstera Deliciosa")
    content['p'] = p
    return render(request, 'store/index.html', content)


class Store(View):
    def get(self, request):
        content = {}
        products = Product.objects.filter(is_active=True)
        for p in products:
            temp = [p.name, p.price, p.image]
            attributes = Product_Attribute.objects.all().filter(id_product=p.id)
            attributes_temp = []
            for a in attributes:
                attr = Attribute.objects.get(id=a.id_attribute.id)
                attributes_temp.append(attr.name)
            temp.append(attributes_temp)
            p.attributes = attributes_temp

        content['products'] = products
        # print(products_temp)
        return render(request, 'store/store.html', content)

    def post(self, request):
        pass
