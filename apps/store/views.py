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


# Create your views here.
# @login_required(login_url="/login/")
def home_page(request):
    content = {}
    p = Product.objects.get(name="Monstera Deliciosa")
    content['p'] = p
    return render(request, 'store/index.html', content)


class Store(View):
    def get(self, request):
        content = {}
        products = Product.objects.all()
        products_temp = []
        for p in products:
            temp = [p.name, p.price, p.image]
            attributes = Product_Attribute.objects.all().filter(id_product=p.id)
            attributes_temp = []
            for a in attributes:
                attr = Attribute.objects.get(id=a.id_attribute.id)
                attributes_temp.append(attr.name)
            temp.append(attributes_temp)
            products_temp.append(temp)
        content['products'] = products
        # print(products_temp)
        return render(request, 'store/store.html', content)

    def post(self, request):
        pass


class Account(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        content = {}

        # print(products_temp)
        return render(request, 'store/account.html', content)

    def post(self, request):
        pass