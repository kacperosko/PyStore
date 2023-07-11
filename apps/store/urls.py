# -*- encoding: utf-8 -*-

from django.urls import path, re_path


from apps.store import views

urlpatterns = [
    path('', views.home_page, name='store'),
    path('store', views.Store.as_view(), name='store'),
    path('about-us', views.about_us),
    path('store/<product_url>', views.get_product),
    path('ajax/settheme', views.set_theme, name='cart_getdiscount'),

    # re_path(r'^.*\.*', views.pages, name='pages'),
]

