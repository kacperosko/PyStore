# -*- encoding: utf-8 -*-

from django.urls import path, re_path


from apps.account import views

urlpatterns = [
    path('account/', views.get_user_account),
    path('account/your-orders', views.get_user_account_orders),
    path('account/your-orders/order-<order_id>', views.get_user_account_order),
    path('account/saved-addresses', views.get_user_saved_addresses),
    path('account/saved-addresses/address-<order_id>', views.get_user_account_order),
    path('ajax/showaddresses', views.get_user_addresses),
    path('ajax/chooseaddress', views.choose_address),
    path('ajax/saveaddress', views.save_address),
]

