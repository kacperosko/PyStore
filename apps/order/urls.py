# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.order import views


urlpatterns = [
    path('cart', views.CartSubtotal.as_view(), name='cart_subtotal'),
    path('cart/checkout', views.CartCheckout.as_view(), name='cart_checkout'),
    path('cart/completed', views.get_completed_order, name='order_completed'),
    path('ajax/addproducttocart', views.add_product_to_cart, name='cart_addproduct'),
    path('ajax/getcartproducts', views.get_carts_product_count, name='cart_getcartsproductcount'),
    path('ajax/removeproduct', views.remove_product, name='cart_removeproduct'),
    path('ajax/adddiscount', views.add_discount, name='cart_adddiscount'),
    path('ajax/deletediscount', views.delete_discount, name='cart_deletediscount'),
    path('ajax/gettotaldiscount', views.get_discount, name='cart_getdiscount'),
]
