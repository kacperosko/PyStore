# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.blog import views


urlpatterns = [
    path('blog', views.get_all_articles, name='blog_articles')
]
