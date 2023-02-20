# -*- encoding: utf-8 -*-

from django.urls import path, re_path


from apps.store import views

urlpatterns = [
    path('', views.home_page, name='store'),
    path('store', views.Store.as_view(), name='store'),
    path('account', views.Account.as_view()),
    # re_path(r'^.*\.*', views.pages, name='pages'),
]

