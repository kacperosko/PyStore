# -*- encoding: utf-8 -*-

from django.urls import path, re_path


from apps.account import views

urlpatterns = [
    path('account/', views.get_user_account),
    path('account/your-orders', views.get_user_account_orders),
    path('account/your-orders/order-<order_id>', views.get_user_account_order),
]

